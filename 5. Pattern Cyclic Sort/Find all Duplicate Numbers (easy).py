'''
Problem Statement 
    We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
    The array has some duplicates, find all the duplicate numbers without using any extra space.

    Example 1:
    Input: [3, 4, 4, 5, 5]
    Output: [4, 5]

    Example 2:
    Input: [5, 4, 7, 2, 3, 5, 3]
    Output: [3, 5]
'''


def find_duplicates(nums):
    fruits = set()

    i = 0
    while i < len(nums):
        # 每个元素各归其位，否则循环，直到归位
        # 如此time complexity of the above algorithm is O(n)
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            if i != j:
                fruits.add(nums[i])
            i = i + 1

    return fruits


def main():
    print(find_duplicates([3, 4, 4, 5, 5]))
    print(find_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()
