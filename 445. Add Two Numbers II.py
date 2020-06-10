'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        stack_l1 = []
        stack_l2 = []
        while l1:
            stack_l1.append(l1.val)
            l1=l1.next
        while l2:
            stack_l2.append(l2.val)
            l2 = l2.next
        head = l3 = ListNode(0)
        carry = 0
        while stack_l1 or stack_l2 or carry:
            if stack_l1:
                carry+=stack_l1.pop()
            if stack_l2:
                carry+=stack_l2.pop()
            l3.val = carry%10
            carry =carry // 10
            if stack_l1 or stack_l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev    
        '''
        def convert_linkedlist_number(l):
            ans = 0
            while l:
                ans = ans *10 + l.val
                l = l.next
            return ans
        def convert_number_linkedlist(number):
            
            head = l3 = ListNode(0)
            number = str(number)
            for i in range(len(number)):
                l3.val = int(number[i])
                if i < len(number)-1:
                    l3.next = ListNode(0)
                    l3 = l3.next
            return head
            
        l1 = convert_linkedlist_number(l1)
        l2 = convert_linkedlist_number(l2)
        
        return convert_number_linkedlist(l1+l2)
        
