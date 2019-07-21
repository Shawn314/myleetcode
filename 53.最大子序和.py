#,4,-1,2,1
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (45.72%)
# Total Accepted:    70.6K
# Total Submissions: 153.2K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        dp = nums.copy()
        for i in range(1, length):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)
        # max_val = nums[0]
        # ans = nums[0]
        # length = len(nums)
        # if length <= 1:
        #     return max_val
        # for i in range(1, length):
        #     if max_val > 0:
        #         max_val += nums[i]
        #     else:
        #         max_val = nums[i]
        #     ans = max(max_val, ans)
        # return ans



        

        
 
