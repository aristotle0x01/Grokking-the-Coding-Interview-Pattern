'''
Problem Statement

There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite
tasks which need to be completed before it can be scheduled. Given the number of tasks
and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Example 1:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2]
0 -> 1 -> 2

1 -> 0
2 -> 1

Example 2:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.
1 -> 0
2 -> 1
0 -> 2


Example 3:
Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible scHeduling of tasks is: [0 1 4 3 2 5]

5 -> 2
5 -> 0
4 -> 0
5 -> 1
2 -> 3
1 -> 3

1 ->3 -> 2 -> 5
0 -> 5
0 -> 4
1 -> 4
'''


def is_scheduling_possible(num, tasks):
    # per_task_dic = {1:[0], 2:[1], 0:[2]}
    per_task_dic = {}

    for t in tasks:
        if t[1] in per_task_dic:
            per_task_dic[t[1]].append(t[0])
        else:
            per_task_dic[t[1]] = [t[0]]

    for k in per_task_dic.keys():
        array = per_task_dic[k]
        temp = []
        for kd in array:
            if kd in per_task_dic:
                temp.extend(per_task_dic[kd])

        while len(temp) > 0:
            t = temp[0]
            if t == k:
                return False

            if t in per_task_dic:
                temp.extend(per_task_dic[t])

            del temp[0]

    return True


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

main()

