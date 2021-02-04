/*
Problem Statement 
    Given an array of positive numbers and a positive number ‘S’, find the length of the smallest 
    contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
    
    Example 1:
    Input: [2, 1, 5, 2, 3, 2], S=7 
    Output: 2
    Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
    
    Example 2:
    Input: [2, 1, 5, 2, 8], S=7 
    Output: 1
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
    
    Example 3:
    Input: [3, 4, 1, 1, 6], S=8 
    Output: 3
    Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
*/

public int solution(int[] array, int s){
            int last_wnd_sum = 0;
            int wnd_size_min = 0;
            int wnd_start = 0;
            int wnd_end = 0;

            int i = 0;
            while (i < array.length){
                last_wnd_sum = last_wnd_sum + array[i];
                if(last_wnd_sum >= s){
                    wnd_end = i;

                    int temp_wnd_size = wnd_end - wnd_start + 1;
                    if(wnd_size_min== 0 || temp_wnd_size < wnd_size_min){
                        wnd_size_min = temp_wnd_size;
                        if(wnd_size_min == 1){
                            return wnd_size_min;
                        }
                    }

                    // minus window start element, then next element sum will be a new total window sum
                    last_wnd_sum = last_wnd_sum - array[wnd_start];

                    if(wnd_start == wnd_end){
                        i++;
                    } else{
                        wnd_start++;
                        last_wnd_sum = last_wnd_sum - array[wnd_end];
                    }
                } else{
                    i++;
                }
            }

            return wnd_size_min;
        }
