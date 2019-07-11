#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (64.69%)
# Total Accepted:    15K
# Total Submissions: 23.1K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
# 
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
# 
# 示例 1:
# 
# 输入: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
# 2
# 输出: 1
# 
# 示例 2:
# 
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# 输出: 3
# 
# 进阶：
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorderTraversal(root, k):
            pStack = []
            cur = root
            cnt = k
            while cur != None or len(pStack) != 0:
                while cur != None:
                    pStack.append(cur)
                    cur = cur.left
                if len(pStack) != 0:
                    cur =  pStack.pop()
                    cnt -= 1
                    if cnt == 0:
                        return cur.val
                    cur = cur.right
            return 0
        return inorderTraversal(root, k)
# if __name__ == '__main__':
#     a = TreeNode(3)
#     l = TreeNode(1)
#     r = TreeNode(4)
#     l2 = TreeNode(2)
#     a.left = l
#     a.right = r
#     l.right = l2
#     s = Solution()
#     import pdb
#     pdb.set_trace()
#     s = Solution()
#     print(s.kthSmallest(a, 4))