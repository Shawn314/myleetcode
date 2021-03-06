#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
# https://leetcode-cn.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (51.96%)
# Total Accepted:    5.3K
# Total Submissions: 10K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给出一个完全二叉树，求出该树的节点个数。
# 
# 说明：
# 
# 
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第
# h 层，则该层包含 1~ 2^h 个节点。
# 
# 示例:
# 
# 输入: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# 输出: 6
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
        # self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0
            return helper(root.left) + helper(root.right) + 1
        if not root:
            return 0
        return helper(root)
# if __name__ == '__main__':
#     s = Solution()
#     a = TreeNode(1)
#     b = TreeNode(2)
#     c = TreeNode(3)
#     a.left = b
#     a.right = c
#     d = TreeNode(4)
#     e = TreeNode(5)
#     f = TreeNode(6)
#     b.left = d
#     b.right = e
#     c.left = f
#     import pdb
#     pdb.set_trace()
#     s = Solution()
#     print(s.countNodes(a))
