'''
Problem Statement
Given a string, sort it based on the decreasing frequency of its characters.

Example 1:
Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

Example 2:
Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.

first get frequency
a -> 2
b -> 3
c -> 1

[a b c]
[3 1 2]

'''

from heapq import *


def sort_character_by_frequency(s):
    dic = {}
    c_array = []

    for c in s:
        if c in dic:
            dic[c] = dic[c] + 1
        else:
            dic[c] = 1
            c_array.append(c)

    frq_array = []
    for c in c_array:
        f = dic[c]
        heappush(frq_array, (-f, c))

    r = ''
    while frq_array:
        fc = heappop(frq_array)
        for i in range(-fc[0]):
            r = r + fc[1]
    return r


def main():
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()

