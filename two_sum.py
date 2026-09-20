def two_sum(numbers, target):
    seen = {}

    for i, number in enumerate(numbers):
        needed = target - number

        if needed in seen:
            return [seen[needed], i]

        seen[number] = i

    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))