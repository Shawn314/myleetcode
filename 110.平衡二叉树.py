#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (48.60%)
# Total Accepted:    21.1K
# Total Submissions: 43.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
# 
# 
# 示例 1:
# 
# 给定二叉树 [3,9,20,null,null,15,7]
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回 true 。
# 
# 示例 2:
# 
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# 返回 false 。
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # level = 0
        self.res = True
        # if not root:
        #     return True
        # def height(root):
        #     if not root:
        #         return 0
        #     return 1 + max(height(root.left), height(root.right))
        # return abs(height(root.left) - height(root.right)) < 2 and
        # self.isBalanced(root.left) and self.isBalanced(root.right)
        def helper(root):
            if not root:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            if abs(left-right) > 1:
                self.res = False
            return max(left, right)
        helper(root)
        return self.res
    
# if __name__ == '__main__':
#     s = Solution()
#     a = TreeNode(3)
#     b = TreeNode(9)
#     c = TreeNode(20)
#     a.left = b
#     a.right = c
#     d = TreeNode(15)
#     e = TreeNode(7)
#     b.left = d
#     # d.left = e
#     import pdb
#     pdb.set_trace()
#     print(s.isBalanced(a))

