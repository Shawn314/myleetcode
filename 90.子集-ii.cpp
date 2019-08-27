/*
 * @lc app=leetcode.cn id=90 lang=cpp
 *
 * [90] 子集 II
 *
 * https://leetcode-cn.com/problems/subsets-ii/description/
 *
 * algorithms
 * Medium (56.20%)
 * Total Accepted:    11.2K
 * Total Submissions: 19.8K
 * Testcase Example:  '[1,2,2]'
 *
 * 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
 * 
 * 说明：解集不能包含重复的子集。
 * 
 * 示例:
 * 
 * 输入: [1,2,2]
 * 输出:
 * [
 * ⁠ [2],
 * ⁠ [1],
 * ⁠ [1,2,2],
 * ⁠ [2,2],
 * ⁠ [1,2],
 * ⁠ []
 * ]
 * 
 */
#include <vector>
#include <set>
using std::vector;
using std::set;

class Solution {
public:
    // traverse result set, and add new item to result set.
    vector<vector<int> > subsetsWithDup2(vector<int>& nums) {
        vector<vector<int> > res;
        vector<int> tmp;
        res.push_back(tmp);
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            int all = res.size();
            for (int j = 0; j < all; j++) {
                vector<int> tmp(res[j]);
                tmp.push_back(nums[i]);
                res.push_back(tmp);
            }
        }
        set<vector<int> > s;
        for (int i = 0; i < res.size(); i++) {
            s.insert(res[i]);
        }
        res.assign(s.begin(), s.end());
        return res;
    }
    vector<vector<int> > subsetsWithDup(vector<int>& nums) {
        vector<vector<int> > res;
        vector<vector<int> > levels;
        vector<int> path; 
        std::sort(nums.begin(), nums.end());
        backtrack(nums, 0, path, res, levels);
        return res;
    }
    void backtrack(vector<int>& nums, size_t start, vector<int>& path, vector<vector<int> >& res, vector<vector<int> > levels) {
        res.push_back(path);
        for (size_t i = start; i < nums.size(); i++) {
            if (i > start && nums[i-1] == nums[i]) {
                continue;
            }
            path.push_back(nums[i]);
            backtrack(nums, i + 1, path, res, levels);
            path.pop_back();
        }
    }
};

// int main() {
//     Solution s;
//     vector<int> nums;
//     nums.push_back(1);
//     nums.push_back(2);
//     nums.push_back(2);
//     vector<vector<int> > res = s.subsetsWithDup(nums);
//     for (int i = 0; i < res.size(); i++) {
//         for (int j = 0; j < res[i].size(); j++) {
//             printf("%d ", res[i][j]);
//         }
//         printf("\n");
//     }
// }

