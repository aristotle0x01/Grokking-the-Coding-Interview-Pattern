
/*
Problem Statement
    Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
    Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
    Example 1:
    Input: [1, 2, 3, 4, 6], target=6
    Output: [1, 3]
    Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

    Example 2:
    Input: [2, 5, 9, 11], target=11
    Output: [0, 2]
    Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
*/

        public int[] solution(int[] sorted, int target){
            int[] a = new int[2];
            a[0] = -1;
            a[1] = -1;

            int n = sorted.length;

            int i1 = 0;
            int i2 = 1;
            while (i2 < n && i1 < n){
                int sum = sorted[i1] + sorted[i2];
                if(sum == target){
                    a[0] = i1;
                    a[1] = i2;
                    break;
                } else if(sum < target){
                    i2++;
                    if(i2 == n){
                        i1++;
                        i2 = i1 + 1;
                    }
                } else {
                    i1++;
                    i2 = i1 + 1;
                }
            }

            return a;
        }
