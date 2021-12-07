// Advent of Code 2021

mod util;
// mod d01;
// mod d02;
mod d05;
// mod d06;
// mod d07;

fn main() {
    // // day 1
    // util::print_ans(d01::part1("../data/01.txt"));  // ans: 1301
    // util::print_ans(d01::part2("../data/01.txt"));  // ans: 1346
    // // day 2
    // util::print_ans(d02::part1("../data/02.txt"));  // ans: 1924923
    // util::print_ans(d02::part2("../data/02.txt"));  // ans: 1982495697
    // day 5
    assert_eq!(d05::part1("../data/05a.txt", true).unwrap(), 5);
    assert_eq!(d05::part1("../data/05.txt", false).unwrap(), 5632);
    assert_eq!(d05::part2("../data/05a.txt", true).unwrap(), 12);
    assert_eq!(d05::part2("../data/05.txt", false).unwrap(), 22213);
    // // day 6
    // assert_eq!(d06::count_dict("../data/06a.txt", 80).unwrap(), 5934);
    // assert_eq!(d06::count_dict("../data/06.txt", 80).unwrap(), 386640);
    // assert_eq!(d06::count_array("../data/06a.txt", 256).unwrap(), 26984457539);
    // assert_eq!(d06::count_array("../data/06.txt", 256).unwrap(), 1733403626279);
    // // day 7
    // assert_eq!(d07::part1("../data/07a.txt").unwrap(), 37);
    // assert_eq!(d07::part1("../data/07.txt").unwrap(), 337833);
    // assert_eq!(d07::part2("../data/07a.txt").unwrap(), 168);
    // assert_eq!(d07::part2("../data/07.txt").unwrap(), 96678050);
}
