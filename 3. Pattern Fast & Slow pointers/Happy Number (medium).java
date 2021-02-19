/*
Problem Statement
    Any number will be called a happy number if,
    after repeatedly replacing it with a number equal to the sum of the square of all of its digits,
    leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
    Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
*/

public boolean happy(int number){
            int sumOfSquares;
            Set<Integer> sequences = new HashSet<>();

            do{
                sumOfSquares = 0;

                while (number != 0){
                    int temp = number % 10;
                    number = number / 10;

                    sumOfSquares = sumOfSquares + temp * temp;
                }

                number = sumOfSquares;

                if(sumOfSquares == 1){
                    return true;
                }else{
                    if(sequences.contains(sumOfSquares)){
                        return false;
                    }else{
                        sequences.add(sumOfSquares);
                    }
                }
            }while (true);
        }
