"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #concatenate the values of l1
        s1=""
        tmp1=l1
        while tmp1:
            s1=s1+str(tmp1.val)
            tmp1=tmp1.next
            
        #concatenate the values of l2
        s2=""
        tmp2=l2
        while tmp2:
            s2=s2+str(tmp2.val)
            tmp2=tmp2.next

        #Convert the concatenated strings to integers and add
        ans=int(s1[::-1])+int(s2[::-1])

        #create a Linked List with output
        dummyRoot = ListNode(0)
        ptr = dummyRoot

        # Reversing the ans as required in Qn
        for number in str(ans)[::-1]:
            ptr.next = ListNode(int(number))
            ptr = ptr.next

        ptr = dummyRoot.next
        return ptr
