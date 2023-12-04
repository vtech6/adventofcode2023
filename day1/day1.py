import re

file = open("./day1/input.txt").read()


numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
words = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]


def parseLine(inputLine: str, includeWords: bool = False):
    filter = numbers.copy()+words.copy() if includeWords else numbers.copy()
    first, last = (999, 0), (-1, 0)
    for nIndex, number in enumerate(filter):
        occurences = [m.start() for m in re.finditer(number, inputLine)]
        if len(occurences) != 0:
            for occurence in occurences:
                first, last = (occurence, nIndex %
                               10) if occurence < first[0] else first, (occurence, nIndex %
                                                                        10) if occurence > last[0] else last

    return 0 if first[0] == 999 else int("{}{}".format(first[1], last[1]))


def solution(input: str):
    lines = file.split("\n")
    print(sum(list(parseLine(line, True) for line in lines)))


solution(file)
