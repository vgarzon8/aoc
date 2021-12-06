// util.rs
// shared utilities

use std::error::Error;
use std::fs::File;
use std::io::Read;
use std::path::Path;
use std::fmt;

#[derive(Debug)]
pub struct MyError {
    details: String,
}

impl MyError {
    pub fn new(msg: &str) -> MyError {
        MyError {
            details: msg.to_string(),
        }
    }
}

impl fmt::Display for MyError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.details)
    }
}

impl Error for MyError {
    fn description(&self) -> &str {
        &self.details
    }
}

pub fn read_lines(input_file: &str) -> Vec<String> {
    let path = Path::new(input_file);
    let mut file = File::open(path).expect("Unable to open file");
    let mut data = String::new();
    file.read_to_string(&mut data)
        .expect("Unable to read string");

    let lines: Vec<String> = data
        .split("\n")
        .map(|x| x.trim())
        .filter(|&x| x.len() > 0)
        .map(|x| x.to_string())
        .collect();

    lines
}

pub fn print_ans(res: Result<i32, MyError>) {
    match res {
        Ok(r) => println!("ans: {}", r),
        Err(e) => println!("{}", e),
    }
}
