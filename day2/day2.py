file = open('./day2/input.txt').read()
colorAmounts = {"red": 12, "green": 13, "blue": 14}


def solution():
    sumOfIds, sumOfPowers = 0, 0
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
                r, g, b = nBalls if nBalls > r and color == "red" else r, nBalls if nBalls > g and color == "green" else g, nBalls if nBalls > b and color == "blue" else b
                if int(nBalls) > colorAmounts[color]:
                    gameInvalid = True

        if not gameInvalid:
            sumOfIds += gameId

        sumOfPowers += r*g*b


solution()
