import two_sum

def test(nums: list, target: int, output: list):
    print("Input: nums = " + str(nums) + ", target = " + str(target))

    result1 = two_sum.two_sum(nums, target)
    result2 = two_sum.two_sum_2(nums, target)

    print("Output (simple): " + str(result1))
    print("Output (hash table): " + str(result2) + "\n")

    assert result1 == output
    assert result2 == output
    
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
