'''
Problem Challenge 1
Quadruple Sum to Target (medium) 
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.
Example 1:
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
Example 2:
Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.
'''

'''
Problem Challenge 1
Quadruple Sum to Target (medium)
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.
Example 1:
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
Example 2:
Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.


[4, 1, 2, -1, 1, -3]

[-3, -1, 1, 1, 2, 4]
'''

'''
首先排序

two pointer
  start      end
  0          n-1

固定两个指针，然后问题变成从start+1 -> end -1 之间寻找两个元素加和为 target - start - end

对找到的元素先放入，最后去重
'''
def find_quadruplets(array, target):
    temp = array.copy()
    list.sort(temp)

    quadruplets = []

    start = 0
    end = len(array) - 1
    while (start + 3) < len(array) and (end - start) >= 3:
        while (end - start) >= 3:
            duals = find_duals(temp, start+1, end-1, target-temp[start]-temp[end])
            for e in duals:
                e.append(temp[start])
                e.append(temp[end])
                list.sort(e)
                quadruplets.append(e)
            end = end - 1

        start = start + 1
        end = len(array) - 1

    d = {}
    q = []
    for e in quadruplets:
        s = ""
        for t in e:
            s = s + str(t)

        if s not in d:
            d[s] = 1
            q.append(e)

    return q

def find_duals(array, start, end, target):
    if start >= (len(array)-1):
        return []
    if end <= 1 or (end-start) < 1:
        return []

    result = []

    si = start
    ei = end
    while ei > si and si < end and ei > start:
        sum = array[si] + array[ei]
        if sum == target:
            result.append([array[si], array[ei]])

            changed = 0

            te = array[ei]
            while ei > 0 and array[ei-1] == te:
                ei = ei - 1
                changed = 1

            se = array[si]
            while si < (len(array)-1) and array[si+1] == se:
                si = si + 1
                changed = 1

            if changed == 0:
                si = si + 1

        if sum > target:
            ei = ei - 1
        if sum < target:
            si = si + 1

    return result


def main():
  print(find_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(find_quadruplets([2, 0, -1, 1, -2, 2], 2))

main()
