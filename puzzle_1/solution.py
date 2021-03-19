class ListNode:
    """This class implements the data structure known as linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        first_node = ListNode(0)
        current_node = first_node
        while l1 or l2 or carry:  # if any digits left, we need more nodes
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            s = val1 + val2 + carry
            carry = int(s/10)

            current_node.next = ListNode(s % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            current_node = current_node.next

        return first_node.next


"""
Solution comments:
The trick here is to work not the current node but with the NEXT node.
Notice how this solution updates not the current node, but the next one
(see line 21).
In my original attempt, I was updating the current node, then preemptively
creating a new one for the next step.

This leads to an issue where a leading 0 is produced in some cases.
By updating the NEXT node, this leading 0 is added at the beginning,
with the first node.
But this first zero can be easily ignored simply by returning first_node.next

Disclaimer: this is based on a sample solution from LeetCode, which helped
improve my own original solution.
I have added the original solution for reference below.
"""


class notGreatSolution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        first_node = ListNode(0)
        current_node = first_node
        while l1 or l2:
            l1 = l1 if l1 else ListNode(0)
            l2 = l2 if l2 else ListNode(0)
            # in the enhanced solution we do not create an auxiliary ListNode
            # we simply interpret the values in the sum as 0 if no more nodes

            s = carry + l1.val + l2.val
            current_node.val = s % 10
            carry = int(s/10)
            l1 = l1.next
            l2 = l2.next

            if l1 or l2:
                current_node.next = ListNode(0)
                current_node = current_node.next

            current_node.next = ListNode(1) if carry else None

        return first_node
