'''
Problem Statement

Given an array of numbers sorted in ascending order,
find the element in the array that has the minimum difference with the given ‘key’.

Example 1:
Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array

Example 2:
Input: [4, 6, 10], key = 4
Output: 4

Example 3:
Input: [1, 3, 8, 13, 15], key = 12
Output: 10

Example 4:
Input: [4, 6, 10], key = 17
Output: 10
'''


def search_min_diff_element(sorted, key):
    start = 0
    end = len(sorted) - 1
    while start < end:
        mid = start + (end - start) // 2
        if sorted[mid] == key:
            return sorted[mid]
        elif sorted[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    if start == end and (end-1) >= 0:
        min = key - sorted[end-1]
        if min < (sorted[end]-key):
            return sorted[end-1]
        else:
            return sorted[end]

    return sorted[end]


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()



'''
Time complexity 
Since, we are reducing the search range by half at every step, 
this means the time complexity of our algorithm will be O(logN) 
where ‘N’ is the total elements in the given array.
Space complexity 
The algorithm runs in constant space O(1).
'''
