def calculateString(params):
    if len(params) == 0:
        return 0
    splittedString = params.split(",")
    numbers = list(map(int, splittedString))
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + numbers[1]
