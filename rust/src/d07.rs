// d06.rs

use crate::util;
use util::MyError;
use std::cmp;

pub fn part1(input_file: &str) -> Result<u32, MyError> {
    let data = parse_lines(util::read_lines(input_file));
    println!("data size {}", data.len());

    // initial search
    let mut fmin: u32 = (data.len() as u32) * 
        data.iter().max().unwrap().pow(2) as u32;

    for k in data.iter() {
        let fuel: i32 = data
            .iter()
            .map(|t: &i32| -> i32{(t - (*k as i32)).abs()})
            .collect::<Vec<i32>>()
            .iter()
            .sum();
        fmin = cmp::min(fmin, fuel as u32);
    }
    Ok(fmin)
}

pub fn part2(input_file: &str) -> Result<u32, MyError> {
    let data = parse_lines(util::read_lines(input_file));

    // initial search
    let mut fmin: u32 = (data.len() as u32) * 
        data.iter().max().unwrap().pow(2) as u32;

    // fuel cost function
    let recur_sum = |n: i32| (n + 1) * n / 2;

    for k in 0..*data.iter().max().unwrap() {
        let fuel: i32 = data
            .iter()
            .map(|t: &i32| recur_sum((t + 1 - (k as i32)).abs()))
            .collect::<Vec<i32>>()
            .iter()
            .sum();
        fmin = cmp::min(fmin, fuel as u32);
    }
    Ok(fmin)
}

fn parse_lines(lines: Vec<String>) -> Vec<i32> {
    lines[0]
        .split(',')
        .map(|t| t.parse::<i32>().expect("failed to parse integer"))
        .collect()
}
