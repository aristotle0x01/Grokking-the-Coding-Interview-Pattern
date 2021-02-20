'''
Problem Challenge 2
    Find the Smallest Missing Positive Number (medium)
    Given an unsorted array containing numbers, find the smallest missing positive number in it.

    Example 1:
    Input: [-3, 1, 5, 4, 2]
    Output: 3
    Explanation: The smallest missing positive number is '3'

    Example 2:
    Input: [3, -2, 0, 1, 2]
    Output: 4

    Example 3:
    Input: [3, 2, 5, 1]
    Output: 4
'''


def find_smallest_missing_positive(nums):
    n = len(nums)
    upper_bound_min = 0

    i = 0
    while i < len(nums):
        # 每个元素各归其位，否则循环，直到归位
        # 如此time complexity of the above algorithm is O(n)
        j = nums[i] - 1
        if j < 0:
            nums[i] = 0
            i = i + 1
        elif j >= n:
            if upper_bound_min == 0:
                upper_bound_min = nums[i]
            if nums[i] < upper_bound_min:
                upper_bound_min = nums[i]

            nums[i] = 0
            i = i + 1
        elif nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            if nums[i] != i+1:
                nums[i] = 0
            i = i + 1

    for i in range(n-1):
        if nums[i] == 0:
            return i+1

    return upper_bound_min - 1


def main():
    print(find_smallest_missing_positive([1, 1, 0, -1, -2]))
    print(find_smallest_missing_positive([3, -2, 0, 1, 2]))
    print(find_smallest_missing_positive([3, 2, 5, 1]))
    print(find_smallest_missing_positive([2, 3, 7, 6, 8, -1, -10, 15]))
    print(find_smallest_missing_positive([-3, 1, 5, 4, 2]))



main()
