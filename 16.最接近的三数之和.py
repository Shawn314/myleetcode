#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (41.08%)
# Total Accepted:    29.8K
# Total Submissions: 72.6K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution:
    def threeSumClosest(self, nums, target):
        length = len(nums)
        if length < 3:
            return 0
        # min_diff = 0
        # closest_val = 0
        # import pdb
        # # pdb.set_trace()
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(0, length-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            head = i+1
            tail = length - 1
            while head < tail:
                sum = nums[i] + nums[head] + nums[tail]
                if sum == target:
                    return sum
                if abs(sum-target) < abs(result-target):
                    result = sum
                elif sum < target:
                    head += 1
                else:
                    tail -= 1
        return result
# if __name__ == '__main__':
#     s = Solution()
#     nums = [1,1,-1,-1,3]
#     print(s.threeSumClosest(nums, 2))
