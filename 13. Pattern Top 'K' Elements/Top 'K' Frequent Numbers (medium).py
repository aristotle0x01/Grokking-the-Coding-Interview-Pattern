'''
Problem Statement 
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
Example 1:
Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:
Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
'''
'''
Problem Statement
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
Example 1:
Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:
Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
'''

from heapq import *


def top_k_freq(nums, k):
    # get frequency
    d = {}
    for e in nums:
        if e in d.keys():
            d[e] = d[e] + 1
        else:
            d[e] = 1

    # get top frequency heap
    minheap = []
    i = 0
    for key in d.keys():
        if i < k:
            heappush(minheap, d[key])
        else:
            if d[key] > minheap[0]:
                heappop(minheap)
                heappush(minheap, d[key])
        i = i + 1

    # using top heap to filter frequency dic
    t = []
    usedkey = {}
    for v in minheap:
        for k in d.keys():
            if k not in usedkey and d[k] == v:
                usedkey[k] = 1
                t.append(k)
                break

    return t


def find_k_frequent_numbers(nums, k):
    # find the frequency of each number
    numFrequencyMap = {}
    for num in nums:
        numFrequencyMap[num] = numFrequencyMap.get(num, 0) + 1

    minHeap = []

    # go through all numbers of the numFrequencyMap and push them in the minHeap, which will have
    # top k frequent numbers. If the heap size is more than k, we remove the smallest(top) number
    for num, frequency in numFrequencyMap.items():
        heappush(minHeap, (frequency, num))
        if len(minHeap) > k:
            heappop(minHeap)

    # create a list of top k numbers
    topNumbers = []
    while minHeap:
        topNumbers.append(heappop(minHeap)[1])

    return topNumbers


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(top_k_freq([1, 3, 5, 12, 11, 12, 11], 1)))

main()
