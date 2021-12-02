// d01.rs
// day 1

use crate::util;
use util::MyError;

// count of sequence increases
pub fn part1(input_file: &str) -> Result<i32, MyError> {

    // // for testing
    // let lines = "\
    //     199
    //     200
    //     208
    //     210
    //     200
    //     207
    //     240
    //     269
    //     260
    //     263
    //     ";
    // let lines: Vec<String> = lines
    //     .split("\n")
    //     .map(|x| x.trim().to_string())
    //     .filter(|x| x.len() > 0)
    //     .collect();
    // println!("{:?}", lines);

    let lines = util::read_file_lines(input_file);
    let data: Vec<i32> = lines
        .iter()
        .map(|x| x.parse::<i32>().expect("failed to parse integer"))
        .collect();

    println!("input file: {}", input_file);
    println!("size {}", data.len());
    println!("first: {:?}", data.first());
    println!("last: {:?}", data.last());

    // python: [dat[k + 1] > dat[k] for k in range(len(dat) - 1)]
    let incr: Vec<_> = data
        .windows(2)
        .map(|x| if x[1] > x[0] {1} else {0})
        .collect();

    // // alternative using iter zip map
    // let incr: Vec<_> = data
    //     .iter()
    //     .zip(&data[1..])
    //     .map(|(&a, &b)| if b > a {1} else {0})
    //     .collect();

    let count_incr = incr.iter().sum::<i32>();

    Ok(count_incr)
}

// Part 2: Find three numbers in list whose product matches argument
pub fn part2(input_file: &str) -> Result<i32, MyError> {

    let lines = util::read_file_lines(input_file);
    let data: Vec<i32> = lines
        .iter()
        .map(|x| x.parse::<i32>().expect("failed to parse integer"))
        .collect();

    let roll_win: Vec<i32> = data
        .windows(3)
        .map(|x| x.iter().sum())
        .collect();

    let incr: Vec<_> = roll_win
        .iter()
        .zip(&roll_win[1..])
        .map(|(&a, &b)| if b > a {1} else {0})
        .collect();

    let count_incr = incr.iter().sum::<i32>();

    Ok(count_incr)
}
