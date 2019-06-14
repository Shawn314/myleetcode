#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (65.49%)
# Total Accepted:    18.3K
# Total Submissions: 27.9K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]  
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3 
# 
# 输出: [3,2,1]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return 
        cur = root
        pStack = []
        result = []
        lstVisit = None
        while cur != None:
            pStack.append(cur)
            cur = cur.left
        while len(pStack) != 0:
            cur = pStack.pop()
            if cur.right == None or cur.right == lstVisit:
                result.append(cur.val)
                lstVisit = cur
            else:
                pStack.append(cur)
                cur = cur.right
                while cur != None:
                    pStack.append(cur)
                    cur = cur.left
        return result
        
        
        


        

