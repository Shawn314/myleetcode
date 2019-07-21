#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (62.41%)
# Total Accepted:    73.5K
# Total Submissions: 117K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummyNode = ListNode(-1)
        dummyNode.next = None
        l1 = None
        l2 = head
        l3 = head
        while l2:
            l3 = l2.next
            l2.next = l1
            l1 = l2
            l2 = l3
        dummyNode.next = l1
        return dummyNode.next
