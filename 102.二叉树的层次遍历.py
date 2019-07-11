#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (56.88%)
# Total Accepted:    31.6K
# Total Submissions: 55.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root) :
        # levels = []
        # if not root:
        #     return levels
        # level = 0
        #DFS 算法
        # def helper(root,level):
        #     if not root:
        #         return
        #     if len(levels) == level:
        #         levels.append([])
        #     levels[level].append(root.val)
        #     helper(root.left, level+1)
        #     helper(root.right,level+1)
        # helper(root, level)
        # return levels
        
        #BFS算法，需要用到队列
        if not root:
            return []
        node_queue = []
        res = []
        node_queue.append(root)
        level = 0
        while len(node_queue) != 0:
            if level == len(res):
                res.append([])
            iter_num = len(node_queue)
            for i in range(iter_num):
                node = node_queue.pop(0)
                res[level].append(node.val)
                if node.left != None:
                    node_queue.append(node.left)
                if node.right != None:
                    node_queue.append(node.right)
            level += 1
        return res
# if __name__ == '__main__':
#     a = TreeNode(1)
#     b = TreeNode(2)
#     c = TreeNode(3)
#     a.left = b
#     a.right = c
#     d = TreeNode(4)
#     e = TreeNode(5)
#     b.left = d
#     b.right = e
#     s = Solution()
#     import pdb
#     pdb.set_trace()
#     print(s.levelOrder(a))



        