'''
Problem Challenge 1

Next Interval (hard)
Given an array of intervals, find the next interval of each interval. In a list of intervals,
for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

Write a function to return an array containing indices of the next interval of each input interval.
If there is no next interval of a given interval, return -1.
It is given that none of the intervals have the same start point.

Example 1:
Input: Intervals [[2,3], [3,4], [5,6]]
Output: [1, 2, -1]
Explanation: The next interval of [2,3] is [3,4] having index ‘1’. Similarly, the next interval of [3,4] is [5,6] having index ‘2’. There is no next interval for [5,6] hence we have ‘-1’.

Example 2:
Input: Intervals [[3,4], [1,5], [4,6]]
Output: [2, -1, -1]
Explanation: The next interval of [3,4] is [4,6] which has index ‘2’. There is no next interval for [1,5] and [4,6].
'''
import heapq
from heapq import *

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


def find_next_interval(intervals):
    r = []

    min_heap = []
    i = 0
    for e in intervals:
        heapq.heappush(min_heap, (e.start, i))
        i = i + 1

    temp = []
    for e in intervals:
        while min_heap and min_heap[0][0] < e.end:
            temp.append(heapq.heappop(min_heap))

        if len(min_heap) > 0:
            r.append(min_heap[0][1])
        else:
            r.append(-1)

        while len(temp) > 0:
            heapq.heappush(min_heap, temp[0])
            del temp[0]

    return r


# brutal force
def find_next_interval2(intervals):
    result = []
    for i in range(len(intervals)):
        interval = intervals[i]

        loop_result = []
        for j in range(len(intervals)):
            if j == i:
                continue

            j_interval = intervals[j]
            if j_interval.start >= interval.end:
                loop_result.append(j_interval)

        if len(loop_result) > 0:
            loop_result = sorted(loop_result, key=lambda x: x.start)
            result.append(loop_result[0])
        else:
            result.append(Interval(None, None))

    r = []
    for i in range(len(result)):
        interval = result[i]
        if interval.start is None:
            r.append(-1)
        else:
            for j in range(len(intervals)):
                j_interval = intervals[j]
                if j_interval.start == interval.start and j_interval.end == interval.end:
                    r.append(j)
                    break
    return r

def main():

  result = find_next_interval([Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval([Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))


main()
