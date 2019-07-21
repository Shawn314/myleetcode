#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (44.38%)
# Total Accepted:    54.9K
# Total Submissions: 123.1K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
#
class Solution:
    def merge(self, nums1, m: int, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(m, m+n):
        #     nums1[i] = nums2[i - m]
        # nums1.sort()
        nums = nums1[:m]
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if nums[i] > nums2[j]:
                nums1[k] = nums2[j]
                j += 1
            else:
                nums1[k] = nums[i]
                i += 1
            k += 1
        while i < m:
            nums1[k] = nums[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
# if __name__ == "__main__":
#     s = Solution()
#     import pdb
#     pdb.set_trace()
    # s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

