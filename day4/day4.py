file = open("day4/input.txt").read()

testCase = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''
# 4 -> {0: 1}, {1: 1}, {2: 1}, {3: 1}, {4: 1}
# 2 -> {0: 1}, {1: 1}, {2: 2}, {3: 2}, {4: 1}
# 2 -> {0: 1}, {1: 1}, {2: 2}, {3: 4}, {4: 2}


def solution(file: str):
    totalScore = 0
    cardScores = {}
    scratchCards = dict({})
    for lineIndex, line in enumerate(file.split("\n")):
        if line != "":
            scratchCards.update({lineIndex: 1})
            card, allNumbers = line.split(":")
            winning, mine = [[int(number) for number in numbers.split(" ") if number != ""]
                             for numbers in allNumbers.split("|")]
            hit = []
            score = 0
            matching = 0
            for number in mine:
                if number in winning:
                    hit.append(number)
            if len(hit) > 0:
                score = 1
                matching = len(hit)
                if len(hit) > 1:
                    score = 2**(len(hit)-1)
            cardScores.update({card: matching})

            totalScore += score
    cardValues = cardScores.values()
    for valueIndex, value in enumerate(cardValues):
        incrementNextCards(scratchCards, valueIndex, value)

    print(cardScores)
    print(totalScore)
    print(scratchCards)
    print(sum(list(scratchCards.values())))


def incrementNextCards(dictionary: dict, currentIndex: int, numberToUpdate: int):
    for step in range(dictionary.get(currentIndex)):
        for i in range(currentIndex+1, currentIndex+numberToUpdate+1):
            currentValue = dictionary.get(i)
            dictionary.update({i: currentValue+1})


solution(file)
