'''
Problem Statement 
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.
Example 1:
Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
Example 2:
Input: [2, 4, 1, 2]
Output: 3
Example 3:
Input: [2, 3, 2, 1]
Output: 4
'''

def find_all_missing_number(array):
    index = 0
    n = len(array)

    while index < n:
        i = array[index] - 1
        if array[index] != (index + 1):
            # 存在冗余，跳出死循环，此时下标index元素没有交换位置
            # 但是迟早会被该在那个位置上的元素交换，除非那个位置上的元素缺失
            if array[i] == array[index]:
                index = index + 1
                continue

            array[i], array[index] = array[index], array[i]
        else:
            index = index + 1

    r = []
    for i in range(len(array)):
        if array[i] != (i+1):
            r.append(i+1)
    return r


def main():
  print(find_all_missing_number([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_all_missing_number([2, 4, 1, 2]))
  print(find_all_missing_number([2, 3, 2, 1]))


main()
