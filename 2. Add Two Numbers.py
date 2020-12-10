# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = current = ListNode(0)
        
        counter = 0
        
        while l1 or l2 or counter:
            v1 = v2 = 0
            
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            ans = v1 + v2 + counter
            counter = ans // 10
            nodeValue = ans % 10
            current.next = ListNode(nodeValue)
            current = current.next
        
        return dummyHead.next

'''
Runtime = 60 ms
Memory = 14.2 MB
'''