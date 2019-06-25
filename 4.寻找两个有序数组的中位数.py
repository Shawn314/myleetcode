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
import pdb
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        n = len(nums1)
        m = len(nums2)
        #保证数组1一定最短
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        # Ci 为第i个数组的割,比如C1为2时表示第1个数组只有2个元素。LMaxi为第i个数组割后的左元素。RMini为第i个数组割后的右元素。
        LMax1, LMax2, RMin1, RMin2 = 0,0,0,0
        # 我们目前是虚拟加了'#'所以数组1是2*n长度
        c1,c2,lo,hi = 0, 0, 0, 2 * n
        while lo <= hi:
            c1 = (lo + hi) // 2
            c2 = (2n + 2m) / 2 - c1
            if c1 == 0:
                LMax1 = -sys.maxsize - 1
            else:
                LMax1 = nums1[(int)((c1 - 1) // 2)]
            if c1 == 2 * n:
                RMin1 = sys.maxsize
            else:
                RMin1 = nums1[(int)(c1 // 2)]
            if c2 == 0:
                LMax2 = -sys.maxsize - 1
            else:
                LMax2 = nums2[(int)((c2 - 1) // 2)]
            if c2 == 2 * m:
                RMin2 = sys.maxsize
            else:
               RMin2 = nums2[(int)(c2 // 2)]

            if LMax1 > RMin2:
                hi = c1 - 1
            elif LMax2 > RMin1:
                lo = c1 +1
            else:
                break
        # pdb.set_trace()
        return (max(LMax1,LMax2) + min(RMin1, RMin2)) / 2.0
# if __name__ == '__main__':
#     s = Solution()
#     pdb.set_trace()
#     print(s.findMedianSortedArrays([2,3,5], [1,4,7,9]))