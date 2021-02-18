/*
Problem Statement
    Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
    If the total number of nodes in the LinkedList is even, return the second middle node.

    Example 1:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
    Output: 3

    Example 2:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
    Output: 4

    Example 3:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
    Output: 4
*/


public ListNode getMiddle(ListNode head){
        ListNode p1=null,p2=null;
        do{
            if(p2 == null){
                p1 = head;
                p2 = head.next;
            }else {
                if(p2.next != null){
                    p2 = p2.next.next;
                }else{
                    p2 = p2.next;
                }
                p1 = p1.next;
            }
        }while (p2 != null);

        return p1;
    }
