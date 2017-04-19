def find_max_min(numbers):
    """get an array containing the maximum and minimum number from a list of numbers provided"""
    minimum = None
    maximum = None

    for i in numbers:
        if minimum is None or minimum > i:
            minimum = i
        if maximum is None or maximum < i:
            maximum = i
    return [minimum, maximum] if minimum != maximum else [len(numbers)]
