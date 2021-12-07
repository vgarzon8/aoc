// d05.rs

use regex::Regex;
use ndarray::prelude::Array;
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


// def part1(input_file, debug=False):
//     dat = prep_data(input_file)
//     g = Map(dat)
//     g.update_lines("horiz_vert")
//     if debug:
//         g.print_state()
//     return g.count_overlaps()

pub fn part1(input_file: &str, debug: bool) -> Result<i32, MyError> {
    let buf = util::read_lines(input_file);
    println!("input file: {}", input_file);
    println!("lines head: {:?}", &buf[0..3]);
    println!("lines tail: {:?}", &buf[(buf.len() - 3)..]);

    let lines = parse_lines(buf);
    println!("{:?}", lines);

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
    println!("{:?}", grid);

    // from math import atan2, sqrt, sin, cos
    // for k, (beg, end) in enumerate(self.dat):
    //     if mode == "horiz_vert" and beg[0] != end[0] and beg[1] != end[1]:
    //         continue
    //     th = atan2(end[1] - beg[1], end[0] - beg[0])
    //     rmax = sqrt((end[0] - beg[0])**2 + (end[1] - beg[1])**2)
    //     steps = max(abs(end[0] - beg[0]), abs(end[1] - beg[1]))
    //     scl = rmax / steps
    //     for t in range(steps + 1):
    //         x = beg[0] + int(round(scl * t * cos(th)))
    //         y = beg[1] + int(round(scl * t * sin(th)))
    //         self.grid[(x, y)] += 1

    let mode = "horiz_vert";
    // let mode = "";

    for ln in lines.iter() {
        if mode == "horiz_vert" && ln.beg.x != ln.end.x && ln.beg.y != ln.end.y {
            continue;
        }
        let dx = (ln.end.x - ln.beg.x) as f64;
        let dy = (ln.end.y - ln.beg.y) as f64;
        let th = dy.atan2(dx);
        let rmax = (dx.powi(2) + dy.powi(2)).sqrt();
        let steps = (ln.end.x - ln.beg.x).abs().max((ln.end.y - ln.beg.y).abs());
        let scl = rmax / (steps as f64);

        println!("{:?} {} {} {}, {}", ln, th, rmax, steps, scl);

        for t in 0..(steps + 1) {
            let st = scl * (t as f64);
            let ix = ln.beg.x as usize + (st * th.cos()).round() as usize; 
            let iy = ln.beg.y as usize + (st * th.sin()).round() as usize;
            grid[[ix, iy]] += 1;
        }
    }

    println!("{:?}", grid.t());

    println!("{:?}", grid.map(|&x| if x > 1 {1} else {0}).sum());

    // let data = parse_lines(lines);
    // println!("size {}", data.len());
    // println!("first: {:?}", data.first());
    // println!("last: {:?}", data.last());


    Ok(1)
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
