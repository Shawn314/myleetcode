#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (55.57%)
# Total Accepted:    6.4K
# Total Submissions: 11.4K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
# 
# 示例:
# 
# 输入: 3
# 输出:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
1）二叉搜索树：如果根节点有左子树，那么左子树的所有结点值，要小于根节点的值
               如果根节点有右子树，那么右子树的所有结点值，要大于根节点的值
以不同数为 root，这就由 i 左边的数可以构成什么样的二叉搜索树，
i 的右边的数构成什么样的二叉搜索树。

'''
import pdb
class Solution:
    def generateTrees(self, n: int) -> []:
        def helper(tree):
            ans = []
            # 遍历所有可能得根节点
            for i, val in enumerate(tree):
                left, right = tree[:i], tree[i+1:]
                for ltree in helper(left) or [None]:
                    for rtree in helper(right) or [None]:
                        root = TreeNode(val)
                        root.left, root.right = ltree, rtree
                        ans.append(root)
            return ans
        pdb.set_trace()
        return helper(range(1,n+1))
if __name__ == '__main__':
    s = Solution()
    print(s.generateTrees(3))

