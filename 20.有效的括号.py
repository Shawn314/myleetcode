#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.67%)
# Total Accepted:    88K
# Total Submissions: 227.4K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        # right_sym = '}])'
        # stack = []
        # for i in s:
        #     if i in right_sym and len(stack) != 0:
        #         stack_sym = stack.pop()
        #         if (stack_sym == '{' and i != '}') or \
        #            (stack_sym == '[' and i != ']') or\
        #            (stack_sym == '(' and i != ')'):
        #             return False
        #     elif i in right_sym and len(stack) == 0:
        #         return False
        #     else:
        #         stack.append(i)
        # if len(stack) != 0:
        #     return False
        # return True
        stack = []
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '{':
                stack.append('}')
            elif i == '[':
                stack.append(']')
            elif (len(stack) == 0 or stack.pop() != i):
                return False
        return len(stack) == 0
# if __name__ == '__main__':
#     s = Solution()
#     string = '()[]{}'
#     import pdb
#     pdb.set_trace()
#     print(s.isValid(string))