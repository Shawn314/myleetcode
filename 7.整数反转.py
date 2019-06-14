#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (32.48%)
# Total Accepted:    132.4K
# Total Submissions: 407.5K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#

import pdb
# class Solution:
#     def reverse(self, x: int) -> int:
#         if x > -10 and x < 10:
#             return x
#         strInt = str(x)
#         length = len(strInt)
#         pStack = []
#         zeroPass = True
#         for i in strInt:
#             pStack.append(i)
#         result = ''
#         for j in pStack[::-1]:
#             if zeroPass and j == '0':
#                 continue
#             if j != '0':
#                 zeroPass = False
#             if j == '-':
#                 result = -int(result)
#             else:
#                 result += j
#         result = int(result)
#         if result >= pow(2,31)-1 or result <= -pow(2,31):
#             # pdb.set_trace()
#             result = 0
#         return result
class Solution:
    def reverse(self, x: int) -> int:
        tmp = 0
        negtive = False
        max_value = pow(2,31) - 1
        if x < 0:
            negtive = True
            x = -x
        while x != 0:
            tmp = tmp * 10 + x % 10
            if tmp > max_value:
                return 0
            x //= 10
        if negtive:
            tmp = -tmp
        return tmp
# if __name__ == '__main__':
#     s = Solution()
#     x = -123123123211224124
#     print(s.reverse(x))
