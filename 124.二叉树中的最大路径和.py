#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (35.95%)
# Total Accepted:    9.2K
# Total Submissions: 25.4K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
#
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
#
# 示例 1:
#
# 输入: [1,2,3]
#
# ⁠      1
# ⁠     / \
# ⁠    2   3
#
# 输出: 6
#
#
# 示例 2:
#
# 输入: [-10,9,20,null,null,15,7]
#
# -10
# / \
# 9  20
# /  \
# 15   7
#
# 输出: 42
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# from recoveryTree import *

import sys


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = -sys.maxsize - 1
        '''
        def helper(root):
            if not root:
                return 0
            if not root.left and not root.right:
                if root.val > self.maxSum:
                    self.maxSum = root.val
                return root.val
            else:
                left = helper(root.left)
                right = helper(root.right)
                max_val = max(root.val + left, root.val+right,
                              root.val + left + right, root.val)
                if max_val > self.maxSum:
                    self.maxSum = max_val
                if max_val == root.val + left + right:
                    max_val = max(root.val + left, root.val+right,
                                  root.val)
                return max_val
        helper(root)
        return self.maxSum
        '''
        def helper(root):
            if root == None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            value1 = root.val
            value2 = root.val + left
            value3 = root.val + right
            value4 = root.val + left + right

            # 以此为根节点的最大值
            maxValue = max([value1, value2, value3, value4])
            self.maxSum = max(self.maxSum, maxValue)
            return max([value1, value2, value3])
        helper(root)
        return self.maxSum
