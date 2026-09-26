use std::env;
use std::fs;
use std::io::{self, Read};
use code2llm_fast_core::{calculate_complexity, extract_function_body_from_lines};

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut lang = "c_family".to_string();
    let mut file_path: Option<String> = None;
    let mut lines: Vec<usize> = Vec::new();
    let mut i = 1;

    while i < args.len() {
        match args[i].as_str() {
            "--lang" => {
                if i + 1 < args.len() {
                    lang = args[i + 1].clone();
                    i += 1;
                }
            }
            "--file" => {
                if i + 1 < args.len() {
                    file_path = Some(args[i + 1].clone());
                    i += 1;
                }
            }
            "--lines" => {
                if i + 1 < args.len() {
                    lines = args[i + 1]
                        .split(',')
                        .filter_map(|s| s.trim().parse::<usize>().ok())
                        .collect();
                    i += 1;
                }
            }
            "--line" => {
                if i + 1 < args.len() {
                    if let Ok(l) = args[i + 1].trim().parse::<usize>() {
                        lines.push(l);
                    }
                    i += 1;
                }
            }
            _ => {}
        }
        i += 1;
    }

    let content = match file_path {
        Some(path) => match fs::read_to_string(&path) {
            Ok(s) => s,
            Err(e) => {
                eprintln!("Error reading file {}: {}", path, e);
                std::process::exit(1);
            }
        },
        None => {
            let mut buf = String::new();
            if let Err(e) = io::stdin().read_to_string(&mut buf) {
                eprintln!("Error reading stdin: {}", e);
                std::process::exit(1);
            }
            buf
        }
    };

    let lines_vec: Vec<&str> = content.split('\n').collect();
    let mut results: Vec<String> = Vec::with_capacity(lines.len());
    for &start_line in &lines {
        let body = extract_function_body_from_lines(&lines_vec, start_line);
        let (cc, rank) = calculate_complexity(&body, &lang);
        results.push(format!("{{\"line\":{},\"cc\":{},\"rank\":\"{}\"}}", start_line, cc, rank));
    }

    println!("[{}]", results.join(","));
}
