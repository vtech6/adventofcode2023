file = open("day4/input.txt").read()

testCase = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''


def solution(file: str):
    totalScore = 0
    cardScores, scratchCards = {}, {}
    for lineIndex, line in enumerate(file.split("\n")):
        if line != "":
            scratchCards.update({lineIndex: 1})
            card, allNumbers = line.split(":")
            winning, mine = [[int(number) for number in numbers.split(" ") if number != ""]
                             for numbers in allNumbers.split("|")]
            hit = []
            score, matching = 0, 0
            [hit.append(number) for number in mine if number in winning]
            score, matching = 2**(len(hit)-1) if len(
                hit) > 1 else 1 if len(hit) > 0 else 0, len(hit)
            cardScores.update({card: matching})
            totalScore += score
    [[[scratchCards.update({i: scratchCards.get(i)+1})
       for i in range(valueIndex+1, valueIndex+value+1)] for step in range(scratchCards.get(valueIndex))]
     for valueIndex, value in enumerate(cardScores.values())]
    print("Part 1:", totalScore)
    print("Part 2:", sum(list(scratchCards.values())))


solution(file)
