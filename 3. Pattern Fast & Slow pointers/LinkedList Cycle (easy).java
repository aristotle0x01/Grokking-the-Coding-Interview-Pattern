/*
Problem Statement 
    Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
*/

    private static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

public boolean hasCircle(ListNode head){
            ListNode p1=null,p2=null;
            if(head != null){
                p1 = head.next;
                p2 = head.next;
            }
            if(p1 != null){
                p2 = p1.next;
            }
            while (p1 != null && p2 != null){
                if(p1 == p2){
                    return true;
                }

                p1 = p1.next;
                if(p2.next != null){
                    p2 = p2.next.next;
                }else{
                    p2 = null;
                }
            }

            return false;
        }
