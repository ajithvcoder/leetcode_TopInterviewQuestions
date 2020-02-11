class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # output=[head]
        # out = output.pop()
        # print(out)
        prev=None
        current=head
        while (current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        #head=current
        return prev