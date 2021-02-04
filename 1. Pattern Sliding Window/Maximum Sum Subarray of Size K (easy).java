/*    
Problem Statement
    Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
    Example 1:
    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].
    Example 2:
    Input: [2, 3, 4, 1, 5], k=2
    Output: 7
    Explanation: Subarray with maximum sum is [3, 4].
*/

public int solution(int[] array, int k){
            int max = 0;
            int wnd_max = 0;

            for(int i=0; i < array.length; i++){
                wnd_max = wnd_max + array[i];
                if(i >= (k-1)){
                    if(wnd_max > max){
                        max = wnd_max;
                    }

                    // minus window start element, then next element sum will be a new total window sum
                    wnd_max = wnd_max - array[i-(k-1)];
                }
            }

            return max;
        }
