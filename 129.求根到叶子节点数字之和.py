#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#
# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (57.79%)
# Total Accepted:    8.1K
# Total Submissions: 13.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
#
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
#
# 计算从根到叶子节点生成的所有数字之和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例 1:
#
# 输入: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
#
# 示例 2:
#
# 输入: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from recoveryTree import *


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        '''
        self.res = 0
        def helper(root, cur):
            if root:
                tmp = cur * 10 + root.val
                if not root.left and not root.right:
                    self.res += tmp
                else:
                    helper(root.left, tmp)
                    helper(root.right, tmp)
        cur = 0
        helper(root, cur)
        return self.res
        '''
        def helper(root, cur):
            if not root:
                return 0
            if not root.left and not root.right:
                return cur * 10 + root.val
            else:
                return helper(root.left, cur * 10 + root.val) + helper(root.right, cur + root.val)
        return helper(root, 0)


# if __name__ == "__main__":
#     operation = TreeOperation()
#     s = Solution()
#     preorder = [1, 2, 3]
#     inorder = [2, 1, 3]
#     import pdb
#     pdb.set_trace()
#     root = operation.recoveryTreeFromPreOrderAndInOrder(preorder, inorder)
#     preorder1 = []
#     print(operation.preorder(root, preorder1))
#     print(s.sumNumbers(root))
