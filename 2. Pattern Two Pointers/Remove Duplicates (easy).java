/*
Problem Statement
    Given an array of sorted numbers, remove all duplicates from it.
    You should not use any extra space; after removing the duplicates in-place return the new length of the array.

    Example 1:
    Input: [2, 3, 3, 3, 6, 9, 9]
    Output: 4
    Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

    Example 2:
    Input: [2, 2, 2, 11]
    Output: 2
    Explanation: The first two elements after removing the duplicates will be [2, 11].
*/

public int solution(int[] repeat){
            int count = 1;

            int n = repeat.length;

            int i1 = 0;
            int i2 = 1;
            while (i2 < n && i1 < i2){
                if(repeat[i2] == repeat[i1]){
                    i2++;
                }else{
                    count++;
                    i1 = i2;
                    i2++;
                }
            }

            return count;
        }
