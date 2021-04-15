'''
Problem Statement
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
Example 1:
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
'''

'''
use sliding window to select zeros to replace
then from the left of window, start counting continuous ones

对于滑动窗口
    如果0不足k个，那么说明1是连续的
    如果0多于k个，那么一定是连续的填充k个0能构成最大连续的1，否则悖论就是将临近的一个0填充，那将比最大的连续1更长
'''
def replace_zero_to_find_longest_continuous_ones(array, k):
    wnd_start = 0
    max_continuous_ones = 0

    n = len(array)
    while wnd_start < n:
        while wnd_start < n and array[wnd_start] == 1:
            wnd_start = wnd_start + 1

        if wnd_start >= n:
            break

        temp = array.copy()

        replaced = 0
        for i in range(wnd_start, n):
            if temp[i] == 0 and replaced < k:
                temp[i] = 1
                replaced = replaced + 1
                if replaced == k:
                    break

        loop_count = count_max_continuous_ones(temp)
        if loop_count > max_continuous_ones:
            max_continuous_ones = loop_count

        wnd_start = wnd_start + 1

    return max_continuous_ones

def count_max_continuous_ones(a):
    max = 0
    temp = 0
    for e in a:
        if e == 1:
            temp = temp + 1
        else:
            if temp > max:
                max = temp
            temp = 0

    if temp > max:
        max = temp
    return max


def main():
  print(replace_zero_to_find_longest_continuous_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(replace_zero_to_find_longest_continuous_ones([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
