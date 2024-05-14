import two_sum

def test(nums: list, target: int, output: list):
    assert two_sum.two_sum(nums, target) == output
    assert two_sum.two_sum_2(nums, target) == output
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output (simple): " + str(two_sum.two_sum(nums, target)))
    print("Output (hash table): " + str(two_sum.two_sum_2(nums, target)) + "\n")
    
def main():
    nums = [2, 7, 11, 15]
    target = 9
    output = [0, 1]
    test(nums, target, output)

    nums = [3, 2, 4]
    target = 6
    output = [1, 2]
    test(nums, target, output)

    nums = [3, 3]
    target = 6
    output = [0, 1]
    test(nums, target, output)

if __name__ == "__main__":
    main()