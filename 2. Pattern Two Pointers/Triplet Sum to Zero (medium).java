/*
Problem Statement
    Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

    Example 1:
    Input: [-3, 0, 1, 2, -1, 1, -2]
    Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
    Explanation: There are four unique triplets whose sum is equal to zero.

    Example 2:
    Input: [-5, 2, -1, -2, 3]
    Output: [[-5, 2, 3], [-2, -1, 3]]
    Explanation: There are two unique triplets whose sum is equal to zero.
*/

        // 1. 原数组排序
        // 2. 循环，逐个固定第一个元素，寻找第二三个元素
        // 3. 问题变成有序数组，查找等值元素
        // 4. 重复元素可以利用hashmap去重

        public List<Integer[]> solution(int[] array){
            Arrays.sort(array);

            List<Integer[]> triplets = new ArrayList<>();

            HashMap<String, Integer> map = new HashMap<>();

            for(int i=0; i < (array.length - 2); i++){
                final int element = array[i];

                List<Integer[]> list = get(array, i + 1, -element);
                list.stream()
                        .forEach(item -> {
                    String key = key(element, item[0], item[1]);
                    if(!map.containsKey(key)){
                        map.put(key, null);

                        Integer[] ii = new Integer[3];
                        ii[0] = element;
                        ii[1] = item[0];
                        ii[2] = item[1];

                        triplets.add(ii);
                    }
                });
            }

            return triplets;
        }

        private List<Integer[]> get(int[] array, int fromIndex, int K){
            List<Integer[]> list = new ArrayList<>();

            int p1 = fromIndex;
            // int p2 = fromIndex + 1;
            int n = array.length;
            int p2 = n - 1;

            while (p1 < p2){
                int sum = array[p1] + array[p2];
                if(sum > K){
                    p2--;
                } else if (sum < K){
                    p1++;
                } else{
                    Integer[] temp = new Integer[2];
                    temp[0] = array[p1];
                    temp[1] = array[p2];
                    list.add(temp);

                    while (p1 < p2){
                        if(array[p1] == array[p1+1]){
                            p1++;
                        }else{
                            p1++;
                            break;
                        }
                    }
                    while (p1 < p2){
                        if(array[p2] == array[p2-1]){
                            p2--;
                        }else{
                            p2--;
                            break;
                        }
                    }
                }
            }

            return list;
        }

        private String key(int i1, int i2, int i3){
            return "" + i1 + "-" + i2 + "-" + i3;
        }
