'''
Problem Statement 
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
Example 1:
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:
Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
'''

'''
Problem Statement
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
Example 1:
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:
Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
'''

from heapq import *


def merge_k_sorted_list(arrayOflist):
    minheap = []
    for list in arrayOflist:
        heappush(minheap, (list[0], list))

    result = []
    while len(minheap) > 0:
        (v, list) = heappop(minheap)
        result.append(v)
        del list[0]
        if len(list) > 0:
            heappush(minheap, (list[0], list))

    return result

def main():
    result = merge_k_sorted_list([[2, 6, 8], [3, 6, 7], [1, 3, 4]])
    print(result, end='')

main()
