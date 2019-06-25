#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
# https://leetcode-cn.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (17.10%)
# Total Accepted:    47.8K
# Total Submissions: 278.7K
# Testcase Example:  '"42"'
#
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
# 
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
# 
# 
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
# 
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
# 
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
# 
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。
# 
# 说明：
# 
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。如果数值超过这个范围，qing返回
# INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。
# 
# 示例 1:
# 
# 输入: "42"
# 输出: 42
# 
# 
# 示例 2:
# 
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
# 我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
# 
# 
# 示例 3:
# 
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
# 
# 
# 示例 4:
# 
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
# ⁠    因此无法执行有效的转换。
# 
# 示例 5:
# 
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
# 因此返回 INT_MIN (−2^31) 。
# 
# 
#
import pdb

# class Solution:
#     def myAtoi(self, str: str) -> int:
#         if str == '':
#             return 0
#         validChar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0','-','+']
#         if str[0] not in validChar and str[0] != ' ':
#             return 0
#         firstChar = ''
#         res = ''
#         resIter = 0
#         l = len(str)
#         headblank = True
#         for i, s in enumerate(str):
#             if (s == '' or s == ' ') and headblank:
#                 continue
#             headblank = False
#             if firstChar == '':
#                 firstChar = s
#                 if firstChar not in validChar:
#                     return 0
#                 if firstChar != '-' and firstChar != '+':
#                     res += s
#                 continue
#             else:
#                 # pdb.set_trace()
#                 if s == '-' or s == '+':
#                     break
#                 if s not in validChar or i == l - 1:
#                     if i == l - 1 and s in validChar:
#                         res += s
#                     if res != '':
#                         break
#                     else:
#                         return 0
#                 res += s
#         if res != '':
#             resIter = self.__string2int(res)
#             if firstChar == '-':
#                 resIter = -resIter
#             if resIter > pow(2,31) -1:
#                 return pow(2,31) -1
#             if resIter < -pow(2,31):
#                 return -pow(2,31)
#             return resIter
#         return 0
#     def __string2int(self, str:str) ->int:
#         if str == '':
#             return 0
#         l = len(str)
#         res = 0
#         # dicthash = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,'6':6,'7':7,'8':8,'9':9}
#         for s in str:
#             res += int(s) * pow(10, l-1)
#             l -= 1
#         return res

# import re
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         str = str.lstrip()
#         str = re.findall('^[\+\-0]*\d+', str)
#         # pdb.set_trace()
#         try:
#             result = int(''.join(str))
#             MAX_INT = 2147483647
#             MIN_INT = -2147483648
#             if result > MAX_INT:
#                 return MAX_INT
#             elif result < MIN_INT:
#                 return MIN_INT
#             return result
#         except:
#             return 0
# 1. discard all leading whitespaces
# 2. sigh of the number
# 3. overflow
# 4. invalid input

# recover nums: base = 10 * base + headNum
# reverse nums: base = 10 * base + tailNum
import pdb
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sign, base, i = 1, 0, 0
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        # pdb.set_trace()
        try:
            while s[i] == ' ':
                i += 1
            if s[i] == '-' or s[i] == '+':
                sign = 1 - 2 * (s[i] == '-')
                i += 1
            validNum = [str(j) for j in range(10)]    
            while i < len(s) and s[i] in validNum:
                if base > MAX_INT//10 or (base == MAX_INT // 10 and int(s[i]) > 7):
                    # pdb.set_trace()
                    if sign == 1:
                        return MAX_INT
                    else:
                        return MIN_INT
                base = 10 * base + int(s[i])
                i += 1
            return base * sign
        except:
            return 0
        
# if __name__ == '__main__':
#     s = Solution()
#     print(s.myAtoi('2147483648'))

