def calculateString(params):
    if len(params) == 0:
        return 0
    splittedString = []
    if "\n" in params:
        splittedString = params.split("\n")
    else:
        splittedString = params.split(",")
    numbers = list(map(int, splittedString))
    return sum(numbers)
