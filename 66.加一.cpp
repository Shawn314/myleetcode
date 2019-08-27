/*
 * @lc app=leetcode.cn id=66 lang=cpp
 *
 * [66] 加一
 *
 * https://leetcode-cn.com/problems/plus-one/description/
 *
 * algorithms
 * Easy (40.06%)
 * Total Accepted:    71.8K
 * Total Submissions: 177K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
 * 
 * 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
 * 
 * 你可以假设除了整数 0 之外，这个整数不会以零开头。
 * 
 * 示例 1:
 * 
 * 输入: [1,2,3]
 * 输出: [1,2,4]
 * 解释: 输入数组表示数字 123。
 * 
 * 
 * 示例 2:
 * 
 * 输入: [4,3,2,1]
 * 输出: [4,3,2,2]
 * 解释: 输入数组表示数字 4321。
 * 
 * 
 */
#include <iostream>
#include <vector>
using std::vector;
using std::cout;
using std::endl;
class Solution {
public:
    // overflow if digits have so many nums.
    // so this solution will be discarded.
    vector<int> plusOne2(vector<int>& digits) {
        vector<int> res;
        long long num = 0;
        for (size_t i = 0; i < digits.size(); i++) {
            num = num * 10 + digits[i];
        }
        num += 1;
        while (num > 0) {
            int residue = num % 10;
            res.push_back(residue);
            num /= 10;
        }
        std::reverse(res.begin(), res.end());
        return res;
    }
    // 思路：从后往前遍历，
    // 1）有 carry 则继续遍历；
    // 2）无 carry 则停止遍历直接返回；
    // 3) 最后如果如果没有退出循环的话，则在头部插入一个1。
    // 注意：直接运算的话，会因为数字过多导致 overflow 的情况。
    vector<int> plusOne(vector<int>& digits) {
        bool carry = false;
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (i == digits.size() - 1 || carry) {
                digits[i] += 1;
                if (digits[i] % 10 == 0) {
                    digits[i] = 0;
                    carry = true;
                }else {
                    carry = false;
                    return digits;
                }
            }
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
// int main() {
//     Solution s;
//     vector<int> digits;
//     digits.push_back(9);
//     digits.push_back(9);
//     digits.push_back(9);
//     digits.push_back(6);
//     digits.push_back(5);
//     digits.push_back(4);
//     digits.push_back(3);
//     digits.push_back(2);
//     digits.push_back(1);
//     digits.push_back(0);
//     vector<int> res = s.plusOne(digits);
//     for (size_t i = 0; i < res.size(); i++) {
//         cout << res[i] << endl;
//     }
// }
