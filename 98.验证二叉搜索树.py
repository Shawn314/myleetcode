#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (26.35%)
# Total Accepted:    27.4K
# Total Submissions: 103.4K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
# 
# 
#
# Definition for a binary tree node.

# small tip:  BST中序遍历 的结果是有序递增的，若违反此规则则，出现错误。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    prevNode = None
    def isValidBST(self, root: TreeNode) -> bool:
        return self.inorderTraversal(root)
        # def helper(root):
        #     if root != None:
        #         if helper(root.left) == False:
        #             return False
        #         if Solution.prevNode != None and Solution.prevNode.val >= root.val:
        #             return False
        #         Solution.prevNode = root
        #         if helper(root.right) == False:
        #             return False
        #     return True
        # return helper(root)
        
    def inorderTraversal(self, root):
        if root is None:
            return True
        pStack = []
        cur = root
        preNode = None
        while len(pStack) != 0 or cur != None:
            while cur != None:
                pStack.append(cur)
                cur = cur.left
            if len(pStack) != 0:
                cur = pStack.pop()
                if preNode != None and preNode.val >= cur.val:
                    return False
                preNode = cur
                cur = cur.right
        return True
# if __name__ == '__main__':
    # a = TreeNode(0)
    # l = TreeNode(1)
    # r = TreeNode(3)
    # a.left = l
    # a.right = r
    # s = Solution()
    # import pdb
    # pdb.set_trace()
    # print(s.isValidBST(a))