#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (35.04%)
# Total Accepted:    58.3K
# Total Submissions: 166.5K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#
import sys
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        LMax1 = 0
        LMax2 = 0
        RMin1 = 0
        RMin2 = 0
        c1 = 0
        c2 = 0
        lo = 0
        hi = 2 * n
        while lo < hi:
            c1 = (lo + hi) / 2
            c2 = m + n - c1
            if c1 == 0:
                LMax1 = -sys.maxint - 1
            else:
                LMax1 = nums1[(int)((c1 - 1) // 2)]
            if c1 == 2 * n:
                RMin1 = sys.maxint
            else:
                RMin1 = nums1[(int)(c1 // 2)]
            if c2 == 0:
                LMax2 = -sys.maxint - 1
            else:
                LMax2 = nums2[(int)((c2 - 1) // 2)]
            if c2 == 2 * m:
                RMin2 = sys.maxint
            else:
               RMin2 = nums2[(int)(c2 // 2)]

            if LMax1 > RMin2:
                hi = c1 - 1
            elif LMax2 > RMin1:
                lo = c1 +1
            else:
                break
        return (max(LMax1,LMax2) + min(RMin1, RMin2)) / 2.0

