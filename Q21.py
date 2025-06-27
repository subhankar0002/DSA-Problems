'''
21. Merge Two Sorted Linked Lists................................

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        tail=dummy
        def marge(list1,list2,tail):
            if not list1:
                tail.next=list2
                return 
            if not  list2:
                tail.next=list1
                return
            if list1.val<list2.val:
                tail.next=list1
                marge(list1.next,list2,tail.next)
            elif list1.val>list2.val:
                tail.next=list2
                marge(list1,list2.next,tail.next)
            else:
                tail.next=list1
                marge(list1.next,list2,tail.next)
        marge(list1,list2,tail)
        return dummy.next
