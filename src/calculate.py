import re
def getNumberList(params):
    delimeters = ",|\n"
    startIndex = 0
    if params.startswith('//'):
        startIndex = params.find('\n')
        delimeters = delimeters + "|" + params[2:startIndex]
        startIndex += 1
    splittedString = re.split(delimeters,params[startIndex:])
    return list(map(int, splittedString))

def calculateString(params):
    if len(params) == 0:
        return 0
    numbers = getNumberList(params)
    return sum(numbers)
