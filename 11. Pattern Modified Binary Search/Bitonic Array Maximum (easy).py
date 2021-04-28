'''
Problem Statement

Find the maximum value in a given Bitonic array. An array is considered bitonic
if it is monotonically increasing and then monotonically decreasing. Monotonically
increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Example 1:
Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.

Example 2:
Input: [3, 8, 3, 1]
Output: 8

Example 3:
Input: [1, 3, 8, 12]
Output: 12

Example 4:
Input: [10, 9, 8]
Output: 10
'''

def find_max_in_bitonic_array(bitonic_array):
    start = 0
    end = len(bitonic_array) - 1
    while start < end:
        mid = start + (end - start) // 2
        if bitonic_array[mid] > bitonic_array[mid+1]:
            end = mid
        else:
            start = mid + 1

    return bitonic_array[start]

def find_max_in_bitonic_array2(bitonic_array):
    if bitonic_array is None:
        return None

    max = bitonic_array[0]
    for i in range(1, len(bitonic_array)):
        if bitonic_array[i] < max:
            return max
        else:
            max = bitonic_array[i]

    return max


def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()



'''
Time complexity 
Since we are reducing the search range by half at every step, 
this means that the time complexity of our algorithm will be O(logN)
where ‘N’ is the total elements in the given array.
Space complexity 
The algorithm runs in constant space O(1).
'''
