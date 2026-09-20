def two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Test run
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]