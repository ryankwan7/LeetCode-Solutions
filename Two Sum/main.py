import two_sum

def test(nums: list, target: int):
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output (simple): " + str(two_sum.two_sum(nums, target)))
    print("Output (hash table): " + str(two_sum.two_sum_2(nums, target)) + "\n")
    
def main():
    nums = [2, 7, 11, 15]
    target = 9
    test(nums, target)

    nums = [3, 2, 4]
    target = 6
    test(nums, target)

    nums = [3, 3]
    target = 6
    test(nums, target)

if __name__ == "__main__":
    main()