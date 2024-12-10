from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy

        carry = 0
        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return res.next

def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linkedlist(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    return " -> ".join(result)

solution = Solution()

l1_input = input("Enter first number as a space-separated list: ")
l1 = list(map(int, l1_input.split()))
l1_linkedlist = list_to_linkedlist(l1)

l2_input = input("Enter second number as a space-separated list: ")
l2 = list(map(int, l2_input.split()))
l2_linkedlist = list_to_linkedlist(l2)

result = solution.addTwoNumbers(l1_linkedlist, l2_linkedlist)

print("Result:", print_linkedlist(result))
