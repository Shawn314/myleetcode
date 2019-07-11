#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (38.41%)
# Total Accepted:    62.1K
# Total Submissions: 161.3K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        len_ori = len(haystack)
        len_need = len(needle)
        if len_need > len_ori:
            return -1
        ind = 0
        for i in range(0, len_ori):
            if i + len_need <= len_ori and haystack[i:i + len_need] == needle:
                return i
            elif i + len_need > len_ori:
                return -1
        return -1

# if __name__ == '__main__':
#     haystack = "a"
#     needle = "a"
#     s = Solution()
#     import pdb
#     pdb.set_trace()
#     print(s.strStr(haystack, needle))
    