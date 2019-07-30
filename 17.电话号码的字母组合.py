#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (49.78%)
# Total Accepted:    32.5K
# Total Submissions: 65.2K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 示例:
# 
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
# 
#

# class Solution:
#     # solution1，相当于树的遍历
#     def letterCombinations(self, digits: str):
#         phone = {'2': ['a', 'b', 'c'],
#                  '3': ['d', 'e', 'f'],
#                  '4': ['g', 'h', 'i'],
#                  '5': ['j', 'k', 'l'],
#                  '6': ['m', 'n', 'o'],
#                  '7': ['p', 'q', 'r', 's'],
#                  '8': ['t', 'u', 'v'],
#                  '9': ['w', 'x', 'y', 'z']}
#         def backtrack(combination, next_digits):
#             if len(next_digits) == 0:
#                 output.append(combination)
#             else:
#                 for letter in phone[next_digits[0]]:
#                     backtrack(combination+letter, next_digits[1:])
#         output = []
#         if digits:
#             backtrack('', digits)
#         return output
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        interpret_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        all_combinations = [''] if digits else []
        for digit in digits:
            current_combinations = list()
            for letter in interpret_digit[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination + letter)
            # pdb.set_trace()
            all_combinations = current_combinations
        return all_combinations
    
# if __name__ == '__main__':
#     s = Solution()
#     str = '23'
#     import pdb
#     pdb.set_trace()
#     print(s.letterCombinations(str))




    
        
        
        