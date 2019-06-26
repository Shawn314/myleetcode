#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.54%)
# Total Accepted:    89.6K
# Total Submissions: 265.4K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs: []) -> str:
        size = len(strs)
        if size < 1:
            return ''
        str_pos = 0
        public_pos = 0
        res = ''
        # import pdb
        while True:
            # pdb.set_trace()
            for cnt, i in enumerate(strs):
                if public_pos >= len(i):
                    # pdb.set_trace()
                    return res[:public_pos]
                if cnt == 0:
                    res += i[public_pos]
                else:
                    if i[public_pos] != res[public_pos]:
                        # pdb.set_trace()
                        return res[:public_pos]
            public_pos += 1
# if __name__ == '__main__':
#     s = Solution()
#     print(s.longestCommonPrefix(["ap","apca","ap"]))

