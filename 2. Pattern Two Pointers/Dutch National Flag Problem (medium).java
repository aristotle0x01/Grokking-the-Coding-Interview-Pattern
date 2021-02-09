/*
Problem Statement
    Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects,
    hence, we can’t count 0s, 1s, and 2s to recreate the array.
    The flag of the Netherlands consists of three colors: red, white and blue;
    and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.
    Example 1:
    Input: [1, 0, 2, 1, 0]
    Output: [0 0 1 1 2]

    Example 2:
    Input: [2, 2, 0, 1, 2, 0]
    Output: [0 0 1 2 2 2 ]
*/

// 虽然都是双指针，关键是对边界的处理，或者说是对指针移动的理解
public void solution(int[] array){
            int p1 = 0;
            int p2 = 0;

            int n = array.length;

            int e = 0;
            while (e < 2 && p1 < n){
                while (p1 < n && array[p1] == e){
                    p1++;
                }

                p2 = p1 + 1;

                while (p2 < n){
                    if(array[p2] == e){
                       int temp = array[p1];
                       array[p1] = array[p2];
                       array[p2] = temp;

                       p1++;
                    }

                    p2++;
                }

                e++;
            }
        }
