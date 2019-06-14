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
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # pdb.set_trace()
        longestLen = 0
        longestStr = ''
        cnt = -1
        for i in s:
            cnt += 1
            store = ''
            for j in s[cnt:]:
                store = store + j;
                tmp = store
                tmp = tmp[::-1]
                if store == tmp and len(tmp) > longestLen:
                    longestLen = len(tmp)
                    longestStr = tmp
        return longestStr

# if __name__ == '__main__':
#     s = 'cbbd'
#     solution = Solution()
#     print(solution.longestPalindrome(s))
                    

