'''
Problem Statement #

Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’.
The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

Example 1:
Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

Example 2:
Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.

Example 3:
Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to '17' in the given array.

Example 4:
Input: [4, 6, 10], key = -1
Output: 0
Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.
'''

def ceiling(sorted, key):
    if key < sorted[0]:
        return 0
    if key > sorted[len(sorted)-1]:
        return -1

    start = 0
    end = len(sorted) - 1
    while start < end:
        mid = start + (end - start) // 2
        if sorted[mid] == key:
            return mid
        elif sorted[mid] < key:
            start = mid + 1
        else:
            end = mid

    return end


def main():
  print(ceiling([4, 6, 10], 6))
  print(ceiling([1, 3, 8, 10, 15], 12))
  print(ceiling([4, 6, 10], 17))
  print(ceiling([4, 6, 10], -1))


main()



'''
Time complexity 
Since we are reducing the search range by half at every step, 
this means that the time complexity of our algorithm will be O(logN)
where ‘N’ is the total elements in the given array.
Space complexity 
The algorithm runs in constant space O(1).
'''
