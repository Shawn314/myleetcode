#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (35.91%)
# Total Accepted:    25.6K
# Total Submissions: 71.3K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#


class Solution:
    def fourSum(self, nums, target: int):
        length = len(nums)
        if length < 4:
            return []
        nums.sort()
        res = []
        # 注意剪枝
        for i in range(0, length - 3):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            # 取最小的都比 target 要大
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # 当数组最大的值的和都小于 target，说明 i 这个值还是太小，遍历下一个
            if nums[i] + nums[length-1] + nums[length-2] + nums[length-3] < target:
                continue
            for j in range(i+1, length - 2):
                if j != i + 1 and nums[j - 1] == nums[j]:
                    continue
                # 同理
                if nums[j] + nums[i] + nums[j+1] + nums[j+2] > target:
                    break
                # 同理
                if nums[j] + nums[i] + nums[length-1] + nums[length-2] < target:
                    continue
                twoSum = target - (nums[i] + nums[j])
                start = j + 1
                end = length - 1
                while start < end:
                    if nums[start] + nums[end] == twoSum:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start+1]:
                            start += 1
                        while start < end and nums[end] == nums[end-1]:
                            end -= 1
                        start += 1
                        end -= 1
                    elif nums[start] + nums[end] < twoSum:
                        start += 1
                    elif nums[start] + nums[end] > twoSum:
                        end -= 1
        return res


# if __name__ == '__main__':
#     s = Solution()
#     import pdb
#     pdb.set_trace()
#     print(s.fourSum([0, 4, -5, 2, -2, 4, 2, -1, 4], 12))
