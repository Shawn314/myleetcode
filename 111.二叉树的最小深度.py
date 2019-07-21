#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (39.06%)
# Total Accepted:    22.2K
# Total Submissions: 56.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 叶子结点的定义是左右孩子为同时为 NULL 时叫做叶子结点
# 当左右孩子有一个为空时，返回不为空的节点
# 当左右孩子两个都不为空时，返回较小深度的节点值
# 1) DFS  取左右孩子最小深度。
# 2) BFS, 停止条件为，结点的左右孩子均为空
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def depth(root):
            if not root:
                return 0
            left,right = depth(root.left), depth(root.right)
            min_val = min(left, right)
            if left == 0 or right == 0:
                min_val = max(left, right)
            return 1 + min_val
        return depth(root)



