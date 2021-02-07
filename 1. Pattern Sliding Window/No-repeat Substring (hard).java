/*
Problem Statement
    Given a string, find the length of the longest substring which has no repeating characters.
    Example 1:
    Input: String="aabccbb"
    Output: 3
    Explanation: The longest substring without any repeating characters is "abc".

    Example 2:
    Input: String="abbbb"
    Output: 2
    Explanation: The longest substring without any repeating characters is "ab".

    Example 3:
    Input: String="abccde"
    Output: 3
    Explanation: Longest substrings without any repeating characters are "abc" & "cde".
*/

public int solution(String fruits){
        int max = 0;

        Map<Character, Integer> constraint = new HashMap<>();

        int wnd_start = 0;
        int wnd_end = 0;
        int loop_max = 0;
        int n = fruits.length();
        while (wnd_end < n && wnd_start < n && wnd_start <= wnd_end){
            char c = fruits.charAt(wnd_end++);

            if(constraint.containsKey(c)){
                while (constraint.containsKey(c)){
                    char ts = fruits.charAt(wnd_start++);
                    constraint.remove(ts);
                }

                constraint.put(c, 1);

                loop_max = wnd_end - wnd_start;
                if(loop_max > max){
                    max = loop_max;
                }
            } else{
                constraint.put(c, 1);

                loop_max = wnd_end - wnd_start;
                if(loop_max > max){
                    max = loop_max;
                }
            }
        }

        return max;
    }
