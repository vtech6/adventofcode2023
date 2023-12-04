file = open('./day2/input.txt').read()
colorAmounts = {"red": 12, "green": 13, "blue": 14}

testInput = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''


def parseLines():
    sumOfIds = 0
    sumOfPowers = 0
    for line in file.split("\n"):
        if line == "":
            print("Sum of ids:", sumOfIds)
            print("Sum of powers", sumOfPowers)
            return
        splitLine = line.split(":")
        rounds = splitLine[1].split(";")
        gameId = int(splitLine[0].split(" ")[1])
        gameInvalid = False
        r, g, b = 0, 0, 0
        for round in rounds:
            balls = round.split(",")
            for ballsOfColor in balls:
                nBalls, color = ballsOfColor.strip().split(" ")
                nBalls = int(nBalls)
                if color == "red":
                    r = nBalls if nBalls > r else r
                if color == "green":
                    g = nBalls if nBalls > g else g
                if color == "blue":
                    b = nBalls if nBalls > b else b

                if int(nBalls) > colorAmounts[color]:
                    gameInvalid = True

        if not gameInvalid:
            sumOfIds += gameId

        print("rgb", r, g, b)
        sumOfPowers += r*g*b

# 2499 too low


parseLines()
