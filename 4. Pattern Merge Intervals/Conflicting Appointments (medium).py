'''
Problem Statement 
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
'''

'''
Problem Statement
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
'''

def is_appointments_conflicting(listOfPair):
    list.sort(listOfPair)
    for i in range(1, len(listOfPair)):
        first = listOfPair[i-1]
        second = listOfPair[i]
        if first[1] <= second[0]:
            continue

        return False

    return True


def main():
  print("Can attend all appointments: " + str(is_appointments_conflicting([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + str(is_appointments_conflicting([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + str(is_appointments_conflicting([[4, 5], [2, 3], [3, 6]])))


main()
