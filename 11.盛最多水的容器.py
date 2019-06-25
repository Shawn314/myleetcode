#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (55.89%)
# Total Accepted:    51.8K
# Total Submissions: 92.3K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 
# 说明：你不能倾斜容器，且 n 的值至少为 2。
# 
# 
# 
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 
# 
# 
# 示例:
# 
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
# 
#
# import pdb
# time complexity is o(n2)
# class Solution:
#     def maxArea(self, height: []) -> int:
#         length = len(height)
#         if length < 2:
#             return 0
#         max_area = 0
#         for i in range(1,length):
#             index = i - 1
#             while index >= 0:
#                 min_val = min(height[i], height[index])
#                 gap = i - index;
#                 if min_val * gap > max_area:
#                     max_area = min_val * gap
#                 index -= 1
#         return max_area
class Solution:
    def maxArea(self, height: []) -> int:
        length = len(height)
        if length < 2:
            return 0
        back, front = 0, length - 1
        max_area = 0
        while back < front:
            min_val = min(height[back], height[front])
            if min_val * (front-back) > max_area:
                max_area = min_val * (front-back)
            if min_val == height[back]:
                back += 1
            else:
                front -= 1
        return max_area

        
# if __name__ == '__main__':
#     s = Solution()
#     print(s.maxArea([1,8,6,2,5,4,8,3,7]))
