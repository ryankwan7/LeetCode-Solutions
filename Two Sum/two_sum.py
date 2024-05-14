def two_sum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
def two_sum_2(nums: list, target: int) -> list:
    complements = {}
    for i, num in enumerate(nums):
        if target - num in complements:
            return [complements[target - num], i]
        complements[num] = i
