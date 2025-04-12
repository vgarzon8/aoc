// d10.rs

use std::collections::HashMap;
use crate::util;
use util::MyError;

pub fn syntax_score(input_file: &str) -> Result<(usize, usize), MyError> {
    const TOK_OPEN: [char; 4] = ['(', '[', '{', '<'];
    const TOK_CLOSE: [char; 4] = [')', ']', '}', '>'];
    const COST: [usize; 4] = [3, 57, 1197, 25137];
    const VALUE: [usize; 4] = [1, 2, 3, 4];
    const VAL_MULT: usize = 5;

    let cost: HashMap<char, usize> = TOK_CLOSE.iter().zip(COST.iter())
        .map(|(k, v)| {return (k.clone(), v.clone())}).collect();

    let value: HashMap<char, usize> = TOK_CLOSE.iter().zip(VALUE.iter())
        .map(|(k, v)| {return (k.clone(), v.clone())}).collect();

    let opener: HashMap<char, char> = TOK_CLOSE.iter().zip(TOK_OPEN.iter())
        .map(|(k, v)| {return (k.clone(), v.clone())}).collect();

    let closer: HashMap<char, char> = TOK_OPEN.iter().zip(TOK_CLOSE.iter())
        .map(|(k, v)| {return (k.clone(), v.clone())}).collect();

    let data = parse_lines(util::read_lines(input_file));
    println!("data size: {}", data.len());

    let mut cost_sum = 0_usize;
    let mut vals: Vec<usize> = Vec::new();

    for (k, row) in data.iter().enumerate() {
        // println!("{} {}", k, row.join(""));
        let mut skip_rest: bool = false;
        let mut op: Vec<String> = Vec::new();
        for d in row.iter() {
            if TOK_OPEN.contains(&d.chars().next().unwrap()) {
                // println!("{} open {}", op.join(""), d);
                op.push(d.clone());
            } else {
                let c = op.pop().unwrap().chars().next().unwrap();
                let dr = &d.chars().next().unwrap();
                if c != opener[dr] {
                    cost_sum += cost[dr];
                    skip_rest = true;
                    // println!("{} mismatch {} {} {}", op.join(""), c, dr, cost[dr]);
                    break;
                } else {
                    // println!("{} close {} {}", op.join(""), c, dr);
                }
            }
        }
        if skip_rest {
            continue;
        }
        op.reverse();
        let cl: Vec<_> = op.iter().map(|x| closer[&x.chars().next().unwrap()]).collect();
        let val_row = cl.iter().fold(0, |a, b| VAL_MULT * a + value[&b]);
        // println!("{:?}", val_row);
        vals.push(val_row);
    }

    vals.sort();
    let score = vals[(vals.len() / 2)];
    Ok((cost_sum, score))
}

fn parse_lines(lines: Vec<String>) -> Vec<Vec<String>> {
    let mut data: Vec<Vec<String>> = Vec::new();
    for line in lines.iter() {
        let row: Vec<String> = line.split("").map(|s| s.to_string())
            .filter(|c| c.len() > 0).collect();
        data.push(row);
    }
    data
}
