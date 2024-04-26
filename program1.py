def smallest_missing_positive_integer(nums: list[int]) -> int:
    if not nums:
        return 1
    nums = set(nums)
    i = 1
    while True:
        if i not in nums:
            return i
        i += 1
    pass
