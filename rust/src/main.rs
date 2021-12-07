// Advent of Code 2021

mod util;
// mod d01;
// mod d02;
mod d05;
// mod d06;

fn main() {
    // util::print_ans(d01::part1("../data/01.txt"));  // ans: 1301
    // util::print_ans(d01::part2("../data/01.txt"));  // ans: 1346
    // util::print_ans(d02::part1("../data/02.txt"));  // ans: 1924923
    // util::print_ans(d02::part2("../data/02.txt"));  // ans: 1982495697
    assert_eq!(d05::part1("../data/05a.txt", true).unwrap(), 5);
    assert_eq!(d05::part1("../data/05.txt", false).unwrap(), 5632);
    assert_eq!(d05::part2("../data/05a.txt", true).unwrap(), 12);
    assert_eq!(d05::part2("../data/05.txt", false).unwrap(), 22213);
    // assert_eq!(d06::count_dict("../data/06a.txt", 80).unwrap(), 5934);
    // assert_eq!(d06::count_dict("../data/06.txt", 80).unwrap(), 386640);
    // assert_eq!(d06::count_array("../data/06a.txt", 256).unwrap(), 26984457539);
    // assert_eq!(d06::count_array("../data/06.txt", 256).unwrap(), 1733403626279);
}
