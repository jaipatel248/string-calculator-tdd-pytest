import re

def calculateString(params):
    if len(params) == 0:
        return 0
    splittedString = re.split(",|\n",params)
    numbers = list(map(int, splittedString))
    return sum(numbers)
