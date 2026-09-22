def two_sum(numbers: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(numbers):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []



print(two_sum([2, 7, 11, 15], 9))  