#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (30.30%)
# Total Accepted:    33.3K
# Total Submissions: 109.1K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        lastLength = 0
        for i in range(length - 1, -1, -1):
            if s[i] != ' ':
                lastLength += 1
            elif s[i] == ' ' and lastLength == 0:
                continue
            else:
                return lastLength
        return lastLength

