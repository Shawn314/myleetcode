#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (55.29%)
# Total Accepted:    80.2K
# Total Submissions: 145K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumyNode1 = ListNode(-1)
        dumyNode1.next = l1
        head1 = dumyNode1
        dumyNode2 = ListNode(-1)
        dumyNode2.next = l2
        head2 = dumyNode2
        dumy_res_head = ListNode(-1)
        dumy_res_head.next = None
        res_iter = dumy_res_head
        if head1 != None or head2 != None:
            while head1.next != None and head2.next != None:
                if head1.next.val <= head2.next.val:
                    head1 = head1.next
                    new_node_1 = ListNode(head1.val)
                    res_iter.next = new_node_1
                    res_iter = new_node_1
                else:
                    head2 = head2.next
                    new_node_2 = ListNode(head2.val)
                    res_iter.next = new_node_2
                    res_iter = new_node_2
            while head1.next != None:
                head1 = head1.next
                new_node_1 = ListNode(head1.val)
                res_iter.next = new_node_1
                res_iter = new_node_1
            while head2.next != None:
                head2 = head2.next
                new_node_2 = ListNode(head2.val)
                res_iter.next = new_node_2
                res_iter = new_node_2
        return dumy_res_head.next
                
                
# if __name__ == '__main__':
#     a_1 = ListNode(1)
#     b_1 = ListNode(2)
#     c_1 = ListNode(4)
#     a_1.next = b_1
#     b_1.next = c_1
#     a_2 = ListNode(0)
#     b_2 = ListNode(3)
#     c_2 = ListNode(4)
#     a_2.next = b_2
#     b_2.next = c_2
#     s = Solution()
#     import pdb
#     pdb.set_trace()
#     head = s.mergeTwoLists(a_1, a_2)
#     while head != None:
#         print("%d " % head.val)
#         head = head.next