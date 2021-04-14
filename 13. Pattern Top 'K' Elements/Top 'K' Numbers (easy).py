'''
Problem Statement
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.
Example 1:
Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:
Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
'''
from heapq import *

def find_K_largest_number(nums, k):
  minheap = []
  for i in range(k):
      heappush(minheap, nums[i])

  for i in range(k, len(nums)):
      if nums[i] > minheap[0]:
          heappop(minheap)
          heappush(minheap, nums[i])

  t = []
  for e in minheap:
      t.append(e)
  return t

def find_K_largest_number2(nums, k):
  result = []
  for num in nums:
      heappush(result, -num)

  r = []
  for i in range(k):
      r.append(heappop(result))

  t = []
  for i in r:
      t.append(-i)
  return t

def main():

  print("Here are the top K numbers: " +
        str(find_K_largest_number([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_K_largest_number([5, 12, 11, -1, 12], 2)))


main()
