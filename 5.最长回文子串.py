#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.30%)
# Total Accepted:    65.8K
# Total Submissions: 258.9K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#
import pdb
# voilence way
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # pdb.set_trace()
#         longestLen = 0
#         longestStr = ''
#         cnt = -1
#         for i in s:
#             cnt += 1
#             store = ''
#             for j in s[cnt:]:
#                 store = store + j;
#                 tmp = store
#                 tmp = tmp[::-1]
#                 if store == tmp and len(tmp) > longestLen:
#                     longestLen = len(tmp)
#                     longestStr = tmp
#         return longestStr

#center spread
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 0:
            return ''
        longest_palindrome = 1
        longest_palindrome_str = s[0]
        for i, ch in enumerate(s):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s,size, i, i+1)
            cur_max_prob = palindrome_odd if odd_len > even_len else palindrome_even
            if len(cur_max_prob) > longest_palindrome:
                longest_palindrome = len(cur_max_prob)
                longest_palindrome_str = cur_max_prob
        return longest_palindrome_str
    
    def __center_spread(self, s:str, size:int, left:int, right:int) -> tuple:
        l = left
        r = right
        while l >= 0 and r < size and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r], r - l + 1
# 解决这类 “最优子结构” 问题，考虑使用 “动态规划”。我们只要找准 “状态” 的定义和 “状态转移方程” 就可以了。
# dp问题最主要的是定义状态和找到状态转移方程
# class Solution:
#     def longestPalindrome(self, s):
#         # pdb.set_trace()
#         size = len(s)
#         if size <= 1:
#             return s
#         # 二维 dp 问题
#         # 状态：dp[i,j] : s[i:j] 包括 i，j 表示的字符串是不是回文串
#         dp = [[False for _ in range(size)] for _ in range(size)]
#         longest_l = 1
#         res = s[0]
#         for i in range(1, size):
#             for j in range(i):
#                 # 状态转移方程：如果头尾字符串相等并且中间也是回文
#                 # 或者中间长度小于等于1
#                 # j >= i - 2: 意思是两个数挨着或者隔一个
#                 if s[j] == s[i] and (j >= i-2 or dp[j+1][i-1]):
#                     dp[j][i] = True
#                     if i - j + 1 > longest_l:
#                         longest_l = i - j + 1
#                         res = s[j:i+1]
#         return res

# if __name__ == '__main__':
#     s = 'abccba'
#     solution = Solution()
#     print(solution.longestPalindrome(s))
                    

