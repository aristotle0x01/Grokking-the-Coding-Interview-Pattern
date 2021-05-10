'''
Problem Statement

Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Example 2:
Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.

将各个sorted arrays以(list[0], list)形式放入minheap，逐个pop即可
'''


from heapq import *


def find_Kth_smallest(arrayList, k):
    minheap = []

    for array in arrayList:
        heappush(minheap, (array[0], array))

    for i in range(k):
        (v, array) = heappop(minheap)
        r = v

        del array[0]
        if array:
            heappush(minheap, (array[0], array))

    return r


def main():
    print("Kth smallest number is: " + str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    print("Kth smallest number is: " + str(find_Kth_smallest([[5, 8, 9], [1, 7]], 3)))


main()

