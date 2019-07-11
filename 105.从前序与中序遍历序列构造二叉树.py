#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (58.84%)
# Total Accepted:    16.1K
# Total Submissions: 27.2K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            if root_val in inorder:
                ind = inorder.index(root_val)
                root.left = self.buildTree(preorder, inorder[:ind])
                root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
#     def preorderTraverse(self, root):
#         if root != None:
#             print(root.val)
#             self.preorderTraverse(root.left)
#             self.preorderTraverse(root.right)
#     def inorderTraverse(self, root):
#         if root != None:
#             self.inorderTraverse(root.left)
#             print(root.val)
#             self.inorderTraverse(root.right)
# if __name__ == '__main__':
#     s = Solution()
#     preorder = [3,9,20,15,7]
#     inorder = [9,3,15,20,7]
#     import pdb
#     pdb.set_trace()
#     root = s.buildTree(preorder, inorder)
#     s.preorderTraverse(root)
#     s.inorderTraverse(root)
    