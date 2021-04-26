'''
Problem Statement

For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
Example 1:
Input: N=2
Output: (()), ()()

Example 2:
Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()

n = 0
[]

n = 1
()

n = 2
()() (())

n = 3
()()() (()()) (())() ()(()) ((()))

n = 4
'(()()())'  ((()()))
 ['(((())))', '', '((())())', '((()))()', '(()(()))', ,
 '(()())()',  '(())()()', '()((()))', '()(()())', '()(())()',
 '()()(())', '()()()()']


'(())(())',
'''

import collections

#recursive
def generate_valid_parentheses_mine(num):
    result = []
    generate_valid_parentheses_mine2(num, 0, [], result)
    return result

def generate_valid_parentheses_mine2(num, index, combination, result):
    if index == num*2:
        if is_parentheses_valid(combination):
            result.append(''.join(map(str, combination)))
        return

    t1 = list(combination).copy()
    t1.append('(')
    generate_valid_parentheses_mine2(num, index+1, t1, result)
    t2 = list(combination).copy()
    t2.append(')')
    generate_valid_parentheses_mine2(num, index+1, t2, result)
    return

# 暴力法
#
# 2^n 种可能
# 逐个验证是否合适
def generate_valid_parentheses(n):
    combinations = [[]]
    for i in range(n*2):
        t = []
        for c in combinations:
            t1 = list(c).copy()
            t1.append('(')
            t.append(list(t1))
        for c in combinations:
            t1 = list(c).copy()
            t1.append(')')
            t.append(list(t1))

        combinations.clear()
        combinations.extend(t)

    r = []
    for e in combinations:
        if is_parentheses_valid(e):
            r.append(''.join(map(str, e)))
    return r

def is_parentheses_valid(parentheses):
    t = parentheses.copy()
    q = collections.deque()

    while t:
        v = t[-1]
        del t[-1]

        if v == ')':
            q.append(v)
        else:
            if len(q) == 0:
                return False
            else:
                q.pop()

    if q:
        return False

    return True

#recursive
def generate_valid_parentheses2(num):
  result = []
  parenthesesString = [0 for x in range(2*num)]
  generate_valid_parentheses_rec(num, 0, 0, parenthesesString, 0, result)
  return result


def generate_valid_parentheses_rec(num, openCount, closeCount, parenthesesString, index, result):

  # if we've reached the maximum number of open and close parentheses, add to the result
  if openCount == num and closeCount == num:
    result.append(''.join(parenthesesString))
  else:
    if openCount < num:  # if we can add an open parentheses, add it
      parenthesesString[index] = '('
      generate_valid_parentheses_rec(
        num, openCount + 1, closeCount, parenthesesString, index + 1, result)

    if openCount > closeCount:  # if we can add a close parentheses, add it
      parenthesesString[index] = ')'
      generate_valid_parentheses_rec(
        num, openCount, closeCount + 1, parenthesesString, index + 1, result)

def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses_mine(5)))
  #print("All combinations of balanced parentheses are: " + str(generate_valid_parentheses2(4)))

main()
