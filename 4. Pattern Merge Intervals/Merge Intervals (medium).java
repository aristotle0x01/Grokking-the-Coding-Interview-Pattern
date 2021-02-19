/*
    Example 1:
    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].
    
    Example 2:
    Intervals: [[6,7], [2,4], [5,9]]
    Output: [[2,4], [5,9]]
    Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

    Example 3:
    Intervals: [[1,4], [2,6], [3,5]]
    Output: [[1,6]]
    Explanation: Since all the given intervals overlap, we merged them into one.
*/

public List<Integer[]> mergeInterval(List<Integer[]> array){
            List<Integer[]> list = new ArrayList<>();

            // my comparator
            Comparator<Integer[]> comparator = new Comparator<Integer[]>() {
                @Override
                public int compare(Integer[] o1, Integer[] o2) {
                    int c = o1[0].compareTo(o2[0]);
                    if(c == 0){
                        return o1[1].compareTo(o2[1]);
                    }
                    return c;
                }
            };

            // sort array by first element of each sub array
            Collections.sort(array, comparator);

            // merge
            while (!array.isEmpty()){
                Integer[] e0 = array.get(0);
                int m01 = e0[0];
                int m02 = e0[1];

                int i = 1;
                for(; i<array.size(); i++){
                    Integer[] ei = array.get(i);
                    int mi1 = ei[0];
                    int mi2 = ei[1];

                    if(m02 < mi1){
                        // found interval
                        break;
                    }else{
                        // found intersection
                        if(m02 < mi2){
                            m02 = mi2;
                        }
                    }
                }

                Integer[] t = new Integer[2];
                t[0] = m01;
                t[1] = m02;
                list.add(t);

                while (i > 0){
                    array.remove(0);
                    i--;
                }
            }

            return list;
        }
