/*
Problem Statement #
    Given a string, find the length of the longest substring in it with no more than K distinct characters.
    Example 1:
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".

    Example 2:
    Input: String="araaci", K=1
    Output: 2
    Explanation: The longest substring with no more than '1' distinct characters is "aa".

    Example 3:
    Input: String="cbbebi", K=3
    Output: 5
    Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
*/

public int solution(String fruits, int K){
        int max = 0;

        Map<Character, Integer> constraint = new HashMap<>();

        int wnd_start = 0;
        int wnd_end = 0;
        int loop_max = 0;
        int n = fruits.length();
        while (wnd_end < n && wnd_start < n && wnd_start <= wnd_end){
            char c = fruits.charAt(wnd_end++);

            if(constraint.containsKey(c)){
                Integer t = constraint.get(c);
                constraint.put(c, t+1);

                loop_max = wnd_end - wnd_start;
                if(loop_max > max){
                    max = loop_max;
                }
            } else{
                if(constraint.size() == K){
                    // new fruit type
                    constraint.put(c, 1);

                    while (constraint.size() > K){
                        char ts = fruits.charAt(wnd_start++);
                        if(constraint.get(ts) == 1){
                            constraint.remove(ts);
                        } else{
                            constraint.put(ts, constraint.get(ts) - 1);
                        }
                    }
                }else {
                    constraint.put(c, 1);
                }

                loop_max = wnd_end - wnd_start;
                if(loop_max > max){
                    max = loop_max;
                }
            }
        }

        return max;
    }
