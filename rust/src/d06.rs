// d06.rs

use std::collections::HashMap;
use crate::util;
use util::MyError;

pub fn count_array(input_file: &str, num_days: i64) -> Result<i64, MyError> {
    const LIFE_SPAN: usize = 7;
    const GAP: usize = 2;
    let lines = util::read_lines(input_file);
    println!("input file: {}", input_file);
 
    let data = parse_lines(lines);
    println!("data size {}", data.len());

    let mut count: [i64; (LIFE_SPAN + GAP)] = [0; (LIFE_SPAN + GAP)];
    for fish in data.iter() {
        count[*fish as usize] += 1;
    }
    for _ in 0..num_days {
        let old = count.clone();
        for k in 0..(LIFE_SPAN + 1) {
            count[k] = old[k + 1];
        }
        count[LIFE_SPAN + GAP - 1] = old[0];
        count[LIFE_SPAN - 1] += old[0];
    }
    println!("{:?}", count);
    Ok(count.iter().sum())
}

// in fact HashMap is not needed -- for future ref
pub fn count_dict(input_file: &str, num_days: i64) -> Result<i64, MyError> {

    let lines = util::read_lines(input_file);
    println!("input file: {}", input_file);
 
    let data = parse_lines(lines);
    println!("data size {}", data.len());

    let mut count: HashMap<i32, i64> = HashMap::new();
    for k in 0..9 {
        count.insert(k as i32, 0);
    }
    for fish in data.iter() {
        *count.get_mut(fish).unwrap() += 1;
        // *count.entry(*fish).or_insert(0) += 1;
    }
    for _ in 0..num_days {
        let old = count.clone();
        for k in 0..8 {
            *count.get_mut(&(k as i32)).unwrap() = old[&((k + 1) as i32)];
        }
        *count.get_mut(&8).unwrap() = old[&0];
        *count.get_mut(&6).unwrap() += old[&0];
    }

    println!("{:?}", count);
    let total_count: i64 = count.values().sum();
    Ok(total_count)
}

fn parse_lines(lines: Vec<String>) -> Vec<i32> {
    lines[0]
        .split(',')
        .map(|t| t.parse::<i32>().expect("failed to parse integer"))
        .collect()
}
