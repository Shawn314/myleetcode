#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (56.06%)
# Total Accepted:    116.8K
# Total Submissions: 208.1K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#
import pdb
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         reverse = self.__reverseNum(x)
#         if reverse == x:
#             return True
#         return False    
#     def __reverseNum(self, x:int) -> int:
#         if x < 10 and x > -10:
#             return x
#         result = 0
#         while x > 0:
#             result = result * 10 + x % 10
#             x //= 10
        # return result
# 取头取尾，进行对比
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         div = 1
#         while x / div >= 10:
#             div *= 10
#         while x > 0:
#             left = x // div
#             right = x % 10
#             if left != right:
#                 return False
#             x = (x % div) // 10
#             div //= 100
#         return True
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        res = 0
        # pdb.set_trace()
        while x >= 0:
            res = res * 10 + x % 10
            x //= 10
            if x <= res or x // 10 == 0:
                if res == x or ((res // 10) == x):
                    return True
                else:
                    return False
        return False
# if __name__ == '__main__':
#     s = Solution()
#     print(s.isPalindrome(0))

    