// d11.rs

use ndarray::prelude::Array;
use crate::util;
use util::MyError;

pub fn part1(input_file: &str, niter: usize, all_flash: bool) -> Result<usize, MyError> {

    let data = parse_lines(util::read_lines(input_file));
    println!("data size: {}", data.len());
    // println!("{:?}", data);
    let nri = data.len();
    let nci = data[0].len();
    // println!("{} {}", nri, nci);

    let mut grid = Array::<usize, _>::zeros((nri, nci));
    for j in 0..nri {
        for i in 0..nci {
            grid[[j, i]] = data[j][i]
        }
    }
    println!("{:?}", grid);

    let mut nb: Vec<(isize, isize)> = Vec::new();
    for j in -1..=1 {
        for i in -1..=1 {
            if i == 0 && j == 0 {
                continue;
            }
            nb.push((j, i));
        }
    }
    // println!("{:?}", nb);

    let mut flash_cnt: usize = 0;
    let mut max_iter: usize = 0;
    for t in 0..niter {
        for j in 0..nri {
            for i in 0..nci {
                grid[[j, i]] += 1
            }
        }
        let mut lit: Vec<(usize, usize)> = Vec::new();  // flashed
        let mut lit_old: Vec<(usize, usize)> = Vec::new();  // previous pass
        // update neighbors
        for u in 0..(nri * nci) {
            for j in 0..nri {
                for i in 0..nci {
                    if grid[[j, i]] > 9 {
                        if lit.contains(&(j, i)) {
                            continue;
                        } else {
                            lit.push((j, i));
                        }
                        // visit each neibhbor
                        for (dj, di) in nb.iter() {
                            let jp = (j as isize) + dj;
                            let ip = (i as isize) + di;
                            if ip < 0 || ip >= (nci as isize) || jp < 0 || jp >= (nri as isize) {
                                continue;
                            }
                            grid[[jp as usize, ip as usize]] += 1;
                        }
                    }
                }
            }
            if lit == lit_old {
                break;
            } else {
                lit_old = lit.clone();
            }
        }
        for j in 0..nri {
            for i in 0..nci {
                if grid[[j, i]] > 9 {
                    grid[[j, i]] = 0
                }
            }
        }
        flash_cnt += lit.len();
        // stop if all flashed and mode is all_flash
        if lit.len() == (nri * nci) && all_flash {
            max_iter = t + 1;
            break;
        }

    }
    println!("{:?}", grid);
    Ok(max_iter)
}

fn parse_lines(lines: Vec<String>) -> Vec<Vec<usize>> {
    let mut data: Vec<Vec<usize>> = Vec::new();
    for line in lines.iter() {
        let row: Vec<usize> = line
            .split("")
            .filter(|c| c.len() > 0)
            .map(|s| s.parse().unwrap())
            .collect();
        data.push(row);
    }
    data
}
