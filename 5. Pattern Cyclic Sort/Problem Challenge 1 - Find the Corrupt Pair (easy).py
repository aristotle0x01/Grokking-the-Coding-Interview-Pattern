  
'''
Problem Challenge 1
Find the Corrupt Pair (easy)
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.
Example 1:
Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
Example 2:
Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
'''


def find_corrupt_pair(array):
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
            r.append(array[i])
            r.append(i+1)
            break
    return r


def main():
  print(find_corrupt_pair([3, 1, 2, 5, 2]))
  print(find_corrupt_pair([3, 1, 2, 3, 6, 4]))


main()
