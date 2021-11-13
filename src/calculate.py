import re

def calculateString(params):
    if len(params) == 0:
        return 0
    delimeters = ",|\n"
    startIndex = 0
    if params.startswith('//'):
        startIndex = params.find('\n')
        delimeters = delimeters + "|" + params[2:startIndex]
        startIndex += 1
    splittedString = re.split(delimeters,params[startIndex:])
    numbers = list(map(int, splittedString))
    return sum(numbers)
