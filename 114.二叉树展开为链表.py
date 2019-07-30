#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (62.16%)
# Total Accepted:    8.9K
# Total Submissions: 14.3K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为链表。
# 
# 例如，给定二叉树
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 将其展开为：
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # preorder_list = []
        # def preorder(root):
        #     if not root:
        #         return
        #     preorder_list.append(root)
        #     preorder(root.left)
        #     preorder(root.right)
        # if not root:
        #     return
        # preorder(root)
        # cur = root
        # for i in preorder_list[1:]:
        #     cur.right = i
        #     cur.left = None
        #     cur = cur.right
        # https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--26/
        #Solution1:
        #1) 找到左子树结点最右侧位置
        #2) 将右子树接到上述位置
        #3) 将右子树设置为左子树
        #4) 将左子树设为空
        #5) 更新根节点位置，根节点为根节点的右子树（若左子树为空。则直接考虑下一
        #节点）
        #6) 重复1-5步骤，直到 root 为 None
        '''
        while root:
            # 若左子树为空。则直接考虑下一节点
            if root.left == None:
                continue
            else:
                # 找到左子树结点最右侧位置
                pre = root.left
                while pre.right:
                    pre = pre.right
                # 将此位置设置为 root.right
                pre.right = root.right
                root.right = root.left
                root.left = None
                root = root.right
        '''
        #Solution2:
        # 后续遍历：右子树->左子树->根节点
        # 后续遍历右子树，和先序遍历是相反的
        '''
        preNode = None
        def postorder(root):
            if root:
                postorder(root.right)
                postorder(root.left)
                root.right = preNode
                # 因为结点的左孩子已经被访问了，所以直接设置为空
                root.left = None
                preNode = root
        postorder(root)
        '''
        #Solution3
        # 因为先序遍历修改右孩子会丢失原来的右孩子
        # 所以可以用栈保存右孩子以防止丢失
        # 特殊的先序遍历
        def preorderStack(root):
            stack = []
            stack.append(root)
            pre = None
            while len(stack) != 0:
                node = stack.pop()
                if pre != None:
                    pre.right = node
                    pre.left = None
                if node.right != None:
                    stack.append(node.right)
                if node.left != None:
                    stack.append(node.left)
                pre = node
        