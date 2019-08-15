/*
 * @lc app=leetcode.cn id=31 lang=cpp
 *
 * [31] 下一个排列
 *
 * https://leetcode-cn.com/problems/next-permutation/description/
 *
 * algorithms
 * Medium (31.25%)
 * Total Accepted:    18K
 * Total Submissions: 57.8K
 * Testcase Example:  '[1,2,3]'
 *
 * 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
 * 
 * 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
 * 
 * 必须原地修改，只允许使用额外常数空间。
 * 
 * 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
 * 1,2,3 → 1,3,2
 * 3,2,1 → 1,2,3
 * 1,1,5 → 1,5,1
 * 
 */
#include <iostream>
#include <vector>
using namespace std;
/*
  1) 找到下一个排列，其实就是找到比当前数字大的排列，且差值最小；若当前为降序，
  则下一个排列为反转整个数组；
  2）后续遍历数组，直到找到 a[i-1] < a[i], 右侧为降序数组；
  3）在a[i:]中找到 k 位置元素，使得 a[k] > a[i-1]，因为右侧为降序，反向扫面第一
  个大的即是，swap(a[i], a[k])
  4) 反转 a[i+1:]即可，得到下一个更大的排列。

*/
class Solution {
public:
    void swap(int&a, int& b) {
        a = a ^ b;
        b = a ^ b;
        a = a ^ b;
    }
    void reverse(vector<int>& nums, int start, int end) {
        while (start < end) {
            swap(nums[start], nums[end]);
            start++;
            end--;
        }
    }
    void nextPermutation(vector<int>& nums) {
        size_t size = nums.size();
        size_t i = size - 1;
        for (; i > 0; i--) {
            if (nums[i-1] < nums[i]) {
                int ind = getHigherNumInd(nums, i, nums[i-1]);
                swap(nums[i-1], nums[ind]);
                reverse(nums, i, size-1);
                break;
            }
        }
        if (i == 0) {
            reverse(nums, 0, size-1);
        }
    };

    int getHigherNumInd(vector<int>& nums, int begin, int target) {
        size_t size = nums.size();
        int i = size - 1;
        for (; i >= begin; i--) {
            if (nums[i] > target) {
                break;
            }
        }
        return i;
    }
};
// int main() {
//     vector<int> nums;
//     nums.push_back(1);
//     nums.push_back(2);
//     nums.push_back(3);
//     Solution* s = new Solution();
//     s->nextPermutation(nums);
//     for (int i = 0; i < nums.size(); i++) {
//         cout << nums[i] << endl;
//     }
//     delete s;
// }
