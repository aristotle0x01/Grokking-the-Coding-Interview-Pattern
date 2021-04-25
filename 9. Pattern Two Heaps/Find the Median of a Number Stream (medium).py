
'''
Problem Statement

Design a class to calculate the median of a number stream. The class should have the following two methods:
insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example 1:
1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5

The median is the middle number in a sorted, ascending or descending, list of numbers
and can be more descriptive of that data set than the average. ...
If there is an odd amount of numbers, the median value is the number that is in the middle,
with the same amount of numbers below and above
'''
import heapq

class MedianOfAStream:
    # the lower half
    maxHeap = []
    # the upper half
    minHeap = []

    def insert_num(self, num):
        if len(self.maxHeap) == 0 or num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        t = len(self.maxHeap) + len(self.minHeap)
        if t % 2 == 0:
            while len(self.maxHeap) > len(self.minHeap):
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            while len(self.minHeap) > len(self.maxHeap):
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        else:
            while len(self.maxHeap) > (len(self.minHeap) + 1):
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            while len(self.minHeap) > 0 and len(self.minHeap) > (len(self.maxHeap) - 1):
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def find_median(self):
        total = len(self.maxHeap) + len(self.minHeap)
        if total % 2 != 0:
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2

def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()
