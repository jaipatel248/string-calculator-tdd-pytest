def calculateString(params):
    if len(params) == 0:
        return 0
    numbers = params.split(",")
    if len(numbers) == 1:
        return int(numbers[0])
    else:
        return int(numbers[0]) + int(numbers[1])
