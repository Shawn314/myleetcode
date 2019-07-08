#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (22.56%)
# Total Accepted:    65K
# Total Submissions: 283.2K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
import pdb
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                # 两个指针，头指针是从 i+1开始，防止加入重复的元素
                lo = i+1
                hi = len(nums) - 1
                twoSum = 0 - nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == twoSum:
                        res.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < twoSum:
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        lo += 1
                    else:
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                        hi -= 1
        return res

# if __name__ == '__main__':
#     s = Solution()
#     l = [0,1,1,2]
#     print(s.threeSum(l))
    