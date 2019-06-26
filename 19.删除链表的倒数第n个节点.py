#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (33.79%)
# Total Accepted:    50.3K
# Total Submissions: 147.6K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 
# 示例：
# 
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
# 
# 说明：
# 
# 给定的 n 保证是有效的。
# 
# 进阶：
# 
# 你能尝试使用一趟扫描实现吗？
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n <= 0:
            return head
        dumpHead = ListNode(-1)
        dumpHead.next = head
        left = dumpHead
        right = dumpHead
        tmp = n
        left_prev = None
        while tmp > 0 or right != None:
            if right == None and tmp != 0:
                return dumpHead.next
            right = right.next
            if tmp == 0:
                left_prev = left
                left = left.next
            else:
                tmp -= 1
        if left_prev != None:
            left_after = left.next
            left.next = None
            left_prev.next = left_after
        return dumpHead.next
# import pdb
# if __name__ == '__main__':
#     l1 = ListNode(1)
#     l2 = ListNode(2)
#     l3 = ListNode(3)
#     l4 = ListNode(4)
#     l5 = ListNode(5)
#     l1.next = l2
#     l2.next = l3
#     l3.next = l4
#     l4.next = l5
#     l5.next = None
#     head = l1
#     cur = head
#     while cur != None:
#         print("%d->" % (cur.val), end='')
#         cur = cur.next
#     print('')
#     s = Solution()
#     pdb.set_trace()
#     new_head = s.removeNthFromEnd(head, 1000000)
#     while new_head != None:
#         print("%d->" % (new_head.val), end='')
#         new_head = new_head.next
#     print('')
    
    
            















            