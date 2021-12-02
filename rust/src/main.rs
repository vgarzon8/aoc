// Advent of Code 2021

mod util;
// mod d01;
mod d02;

fn main() {
    // let res = d01::part1("../data/01.txt");  // ans: 1301
    // let res = d01::part2("../data/01.txt");  // ans: 1346
    // let res = d02::part1("../data/02.txt");  // ans: 1924923 
    let res = d02::part2("../data/02.txt");  // ans: 1982495697

    match res {
        Ok(r) => println!("ans: {}", r),
        Err(e) => println!("{}", e),
    };
}
