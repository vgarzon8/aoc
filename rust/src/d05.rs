// d05.rs

use regex::Regex;
use ndarray::prelude::Array;
use std::cmp::PartialEq;
use crate::util;
use util::MyError;

#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}

#[derive(Debug)]
struct Line {
    beg: Point,
    end: Point,
}

#[derive(PartialEq)]
enum Mode {
    HorizVert,
    All
}

pub fn part1(input_file: &str, debug: bool) -> Result<i32, MyError> {
    if debug {
        println!("{}", input_file);
    }
    let lines = parse_lines(util::read_lines(input_file));
    let count = count_overlap(lines, Mode::HorizVert, debug);
    Ok(count)
}

pub fn part2(input_file: &str, debug: bool) -> Result<i32, MyError> {
    if debug {
        println!("{}", input_file);
    }
    let lines = parse_lines(util::read_lines(input_file));
    let count = count_overlap(lines, Mode::All, debug);
    Ok(count)
}

fn count_overlap(lines: Vec<Line>, mode: Mode, debug: bool) -> i32 {
    let xall: Vec<i32> = lines.iter().map(|p| p.beg.x).chain(
        lines.iter().map(|p| p.end.x)
    ).collect();
    let yall: Vec<i32> = lines.iter().map(|p| p.beg.y).chain(
        lines.iter().map(|p| p.end.y)
    ).collect();

    let xmax = xall.iter().max().unwrap();
    let ymax = yall.iter().max().unwrap();
    println!("{:?} {:?}", xmax, ymax);

    let mut grid = Array::<i32, _>::zeros(((xmax + 1) as usize, (ymax + 1) as usize));

    for ln in lines.iter() {
        if (mode == Mode::HorizVert) && (ln.beg.x != ln.end.x) && (ln.beg.y != ln.end.y) {
            continue;
        }
        let dx = (ln.end.x - ln.beg.x) as f64;
        let dy = (ln.end.y - ln.beg.y) as f64;
        let th = dy.atan2(dx);
        let rmax = (dx.powi(2) + dy.powi(2)).sqrt();
        let steps = (ln.end.x - ln.beg.x).abs().max((ln.end.y - ln.beg.y).abs());
        let scl = rmax / (steps as f64);

        if debug {
            println!("{:?} {} {} {}, {}", ln, th, rmax, steps, scl);
        }
        for t in 0..(steps + 1) {
            let st = scl * (t as f64);
            let ix = (ln.beg.x + (st * th.cos()).round() as i32) as usize; 
            let iy = (ln.beg.y + (st * th.sin()).round() as i32) as usize;
            grid[[ix, iy]] += 1;
        }
    }

    if debug {
        println!("{:?}", grid.t());
    }

    grid.map(|&x| if x > 1 {1} else {0}).sum()
}

fn parse_lines(buf: Vec<String>) -> Vec<Line> {
    let re = Regex::new(r#"(\d+),(\d+) -> (\d+),(\d+)"#).unwrap();
    let mut lines: Vec<Line> = Vec::new();
    for text in buf.iter() {
        let pt: Vec<i32> = re
            .captures(text)
            .unwrap()
            .iter()
            .skip(1)
            .map(|c| c.unwrap().as_str().parse().unwrap())
            .collect();
        lines.push(Line {
            beg: Point {x: pt[0], y: pt[1]},
            end: Point {x: pt[2], y: pt[3]},
        })
    }
    lines
}
