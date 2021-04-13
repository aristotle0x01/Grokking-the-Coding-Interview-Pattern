'''
Problem Statement
Given a set of distinct numbers, find all of its permutations.
Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:
{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!n! permutations.
Example 1:
Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
'''

def find_permutations(numbers):
    if len(numbers) == 1:
        return [numbers]

    subsets = []

    for num in numbers:
        sub = numbers.copy()
        sub.remove(num)
        sub_permutations = find_permutations(sub)
        for item in sub_permutations:
            item.insert(0, num)
            subsets.append(list(item))

    return subsets

def main():
  print("Here are all the permutations: " + str(find_permutations([1, 2, 3, 4])))


main()
