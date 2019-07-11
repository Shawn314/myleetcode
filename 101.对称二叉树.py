#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (47.01%)
# Total Accepted:    39.5K
# Total Submissions: 83.7K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # def isSame(left, right):
        #     if left == None and right == None:
        #         return True
        #     if left == None or right == None:
        #         return False
        #     if left.val != right.val:
        #         return False
        #     return isSame(left.left, right.right) and isSame(left.right, right.left)
        # if root == None:
        #     return True
        # return isSame(root.left,root.right)
        if not root:
            return True
        node_queue = [root.left, root.right]
        while node_queue:
            left = node_queue.pop(0)
            right = node_queue.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            node_queue.append(left.left)
            node_queue.append(right.right)
            node_queue.append(left.right)
            node_queue.append(right.left)
        return True
    