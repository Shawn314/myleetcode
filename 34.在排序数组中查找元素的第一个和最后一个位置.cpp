/*
 * @lc app=leetcode.cn id=34 lang=cpp
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 *
 * https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
 *
 * algorithms
 * Medium (37.22%)
 * Total Accepted:    27K
 * Total Submissions: 72.5K
 * Testcase Example:  '[5,7,7,8,8,10]\n8'
 *
 * 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
 * 
 * 你的算法时间复杂度必须是 O(log n) 级别。
 * 
 * 如果数组中不存在目标值，返回 [-1, -1]。
 * 
 * 示例 1:
 * 
 * 输入: nums = [5,7,7,8,8,10], target = 8
 * 输出: [3,4]
 * 
 * 示例 2:
 * 
 * 输入: nums = [5,7,7,8,8,10], target = 6
 * 输出: [-1,-1]
 * 
 */
#include <vector>
#include <stdio.h>
using namespace std;
class Solution {
public:
    //自己写的时间复杂度在 o(n+log(n)) 不满足题目要求
    vector<int> searchRange(vector<int>& nums, int target) {
/*      vector<int> range(2, -1);
        int size = nums.size();
        if (size <= 0) {
            return range;
        }
        int lo = 0;
        int hi = size - 1;
        while (lo <= hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (nums[mid] == target) {
                int res_start = mid;
                int res_end = mid;
                while (res_start - 1 >= lo && nums[res_start - 1] == target) {
                    res_start --;
                }
                while (res_end + 1 <= hi && nums[res_end + 1] == target) {
                    res_end ++;
                }
                range[0] = res_start;
                range[1] = res_end;
                break;
            }else if (nums[mid] > target) {
                hi = mid - 1;
            }else{
                lo = mid + 1;
            }
        }
        return range;*/
        vector<int> range(2, -1);
        int size = nums.size();
        if (size <= 0) {
            return range;
        }
        int lo = 0;
        int hi = size - 1;
        // found target left boundary
        int left_boundary = -1;
        while (lo <= hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (nums[mid] >= target) {
                if (nums[mid] == target) {
                    left_boundary = mid;
                }
                hi = mid - 1;
            }else{
                lo = mid + 1;
            }
        }
        if (left_boundary == -1) {
            return range;
        }
        lo = left_boundary;
        hi = size - 1;
        int right_boundary = -1;
        while (lo <= hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (nums[mid] <= target) {
                if (nums[mid] == target) {
                    right_boundary = mid;
                }
                lo = mid + 1;
            }else {
                hi = mid - 1;
            }
        }
        range[0] = left_boundary;
        range[1] = right_boundary;
        return range;
    }
};

// int main() {
//     Solution* s = new Solution();
//     vector<int> vec;
//     vec.push_back(1);
//     vector<int> res = s->searchRange(vec, 6);
//     for (int i = 0; i < res.size(); i++) {
//         printf("%d ", res[i]);
//     }
//     printf("\n");
//     return 0;
// }
