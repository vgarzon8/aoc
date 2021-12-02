// d02.rs
// day 2

use crate::util;
use util::MyError;

// ...
pub fn part1(input_file: &str) -> Result<i32, MyError> {

    let lines = util::read_file_lines(input_file);
    println!("input file: {}", input_file);
    println!("lines head: {:?}", &lines[0..3]);
    println!("lines tail: {:?}", &lines[(lines.len() - 3)..]);

    let data: Vec<(String, i32)> = lines
        .iter()
        .map(|x| x.split_whitespace().collect())
        .map(|t: Vec<&str>| {(
            t[0].to_string(),
            t[1].parse::<i32>().expect("failed to parse integer"),
        )})
        .collect();

    println!("size {}", data.len());
    println!("first: {:?}", data.first());
    println!("last: {:?}", data.last());

    let mut x = 0;
    let mut y = 0;
    for (action, step) in data.iter() {
        match action.as_str() {
            "forward" => x += step,
            "down" => y += step,
            "up" => y -= step,
            _ => return Err(MyError::new("unrecognized action"))
        }
        // println!("{} {} {} {}", &action, &step, x, y);
    }

    Ok(x * y)
}

// ...
pub fn part2(input_file: &str) -> Result<i32, MyError> {

    let lines = util::read_file_lines(input_file);
    println!("input file: {}", input_file);
    println!("lines head: {:?}", &lines[0..3]);
    println!("lines tail: {:?}", &lines[(lines.len() - 3)..]);

    let data: Vec<(String, i32)> = lines
        .iter()
        .map(|x| x.split_whitespace().collect())
        .map(|t: Vec<&str>| {(
            t[0].to_string(),
            t[1].parse::<i32>().expect("failed to parse integer"),
        )})
        .collect();

    println!("size {}", data.len());
    println!("first: {:?}", data.first());
    println!("last: {:?}", data.last());

    let mut x = 0;
    let mut y = 0;
    let mut aim = 0;
    for (action, step) in data.iter() {
        match action.as_str() {
            "forward" => {
                x += step;
                y += aim * step;        
            },
            "down" => aim += step,
            "up" => aim -= step,
            _ => return Err(MyError::new("unrecognized action"))
        }
    }

    Ok(x * y)
}
