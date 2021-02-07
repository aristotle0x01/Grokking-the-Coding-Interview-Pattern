/*
Problem Statement
    Given an array of characters where each character represents a fruit tree,
    you are given two baskets and your goal is to put maximum number of fruits in each basket.
    The only restriction is that each basket can have only one type of fruit.
    You can start with any tree, but once you have started you can’t skip a tree.
    You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
    Write a function to return the maximum number of fruits in both the baskets.
    Example 1:
    Input: Fruit=['A', 'B', 'C', 'A', 'C']
    Output: 3
    Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

    Example 2:
    Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
    Output: 5
    Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
    This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
*/

public int solution(char[] fruits){
            int max = 0;

            Map<Character, Integer> constraint = new HashMap<>();

            int wnd_start = 0;
            int wnd_end = 0;
            int loop_max = 0;
            int n = fruits.length;
            while (wnd_end < n && wnd_start < n && wnd_start <= wnd_end){
                char c = fruits[wnd_end++];

                if(constraint.containsKey(c)){
                    Integer t = constraint.get(c);
                    constraint.put(c, t+1);

                    loop_max = wnd_end - wnd_start;
                    if(loop_max > max){
                        max = loop_max;
                    }
                } else{
                    if(constraint.size() == 2){
                        // new fruit type
                        constraint.put(c, 1);

                        while (constraint.size() == 3){
                            // b c b c a
                            char ts = fruits[wnd_start++];
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
