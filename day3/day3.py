file = open("./day3/input.txt").read()

testCases = '''...........
467...14...
...*.......
..35..633..
......#....
617*.......
.....+.58..
..592......
......755..
...$.*.....
.664.598...
'''

numbers = '1234567890'


def solution(file: str):
    proximityFieldList, numberList, uniqueNumbersList, gears = [], [], [], []
    splitFile = file.split("\n")
    gearDict = dict({})
    for lineIndex, line in enumerate(splitFile):
        lineIndices, numberIndices = [], []
        for itemIndex, item in enumerate(line):
            if item in numbers:
                numberIndices.append(itemIndex)
                if itemIndex == len(line)-1:
                    lineIndices.append(numberIndices)
            if item not in numbers:
                if numberIndices != []:
                    lineIndices.append(numberIndices)
                    numberIndices = []
                if item != ".":
                    proximityField = [itemIndex-1,
                                      itemIndex+1, lineIndex-1, lineIndex+1]
                    proximityFieldList.append(proximityField)
                    if item == "*":
                        gears.append(proximityField)

        numberList.append(lineIndices)
    for lineIndex, line in enumerate(numberList):
        for proximityIndex, proximity in enumerate(proximityFieldList):
            yRange = range(proximity[2], proximity[3]+1)
            if lineIndex in yRange:
                xRange = range(proximity[0], proximity[1]+1)
                for number in line:
                    if number[0] in xRange or number[-1] in xRange:
                        uniqueNumber = (lineIndex, int(''.join([str(splitFile[lineIndex][digit])
                                                                for digit in number])), number[0])
                        uniqueNumbersList.append(uniqueNumber)
                        if proximity in gears:
                            gearValues = gearDict.get(proximityIndex)
                            gearValues = gearValues + \
                                [uniqueNumber] if gearValues is not None else [
                                    uniqueNumber]
                            gearDict.update({proximityIndex: gearValues})

    print("Gears multiplied:", sum(list([value[0][1]*value[1][1] if len(value)
                                         == 2 else 0 for value in gearDict.values()])))
    print("Sum of linked numbers:", sum(
        [int(number[1]) for number in set(uniqueNumbersList)]))


solution(file)
