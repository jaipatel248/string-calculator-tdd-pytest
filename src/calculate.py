import re

def getNegativeNumbers(numbers):
    negativeNumbers = []
    for number in numbers:
        if number < 0:
            negativeNumbers.append(number)
    return ",".join(map(str, negativeNumbers))

def checkNegative(numbers):
    for number in numbers:
        if number < 0:
            raise ValueError("negatives not allowed "+ getNegativeNumbers(numbers))
    return True

def getNumberList(params):
    delimeters = ",|\n"
    startIndex = 0
    if params.startswith('//'):
        startIndex = params.find('\n')
        delimeters = delimeters + "|" + params[2:startIndex]
        startIndex += 1
    splittedString = re.split(delimeters,params[startIndex:])
    numbers = list(map(int, splittedString))
    checkNegative(numbers)
    return numbers

def calculateString(params):
    if len(params) == 0:
        return 0
    numbers = getNumberList(params)
    return sum(numbers)
