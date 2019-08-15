/*
 * @lc app=leetcode.cn id=39 lang=cpp
 *
 * [39] 组合总和
 *
 * https://leetcode-cn.com/problems/combination-sum/description/
 *
 * algorithms
 * Medium (66.54%)
 * Total Accepted:    27.4K
 * Total Submissions: 41.1K
 * Testcase Example:  '[2,3,6,7]\n7'
 *
 * 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
 * 
 * candidates 中的数字可以无限制重复被选取。
 * 
 * 说明：
 * 
 * 
 * 所有数字（包括 target）都是正整数。
 * 解集不能包含重复的组合。 
 * 
 * 
 * 示例 1:
 * 
 * 输入: candidates = [2,3,6,7], target = 7,
 * 所求解集为:
 * [
 * ⁠ [7],
 * ⁠ [2,2,3]
 * ]
 * 
 * 
 * 示例 2:
 * 
 * 输入: candidates = [2,3,5], target = 8,
 * 所求解集为:
 * [
 * [2,2,2,2],
 * [2,3,3],
 * [3,5]
 * ]
 * 
 */
/*
  
*/
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;
class Solution {
public:
    /*
    vector<vector<int> > combinationSum(vector<int>& candidates, int target) {
        vector<vector<int> > res;
        int size = candidates.size();
        if (size <= 0) {
            return res;
        }
        vector<int> path;
        sort(candidates.begin(), candidates.end());
        dfs(candidates, 0, size, path, res, target);
        return res;
    }
    void dfs(vector<int>& candidates, int begin, int size, vector<int>& path, vector<vector<int> >& res, int target) {
        if (target == 0) {
            // vector<int> tmp(path);
            res.push_back(path);
        }
        for (int i = begin; i < size; i++) {
            int remain = target - candidates[i];
            if (remain < 0) {
                break;
            }
            path.push_back(candidates[i]);
            dfs(candidates, i, size, path, res, remain);
            path.pop_back();
        }
        }*/
    vector<vector<int> > combinationSum(vector<int>& candidates, int target) {
        vector<vector<int> > res;
        int size = candidates.size();
        if (size <= 0) {
            return res;
        }
        vector<int> path;
        sort(candidates.begin(), candidates.end());
        int cur = 0;
        dfs(candidates, 0, size, path, res, cur, target);
        return res;
    }
    void dfs(vector<int>& candidates, int begin, int size, vector<int>& path, vector<vector<int> >& res, int cur, int target) {
        if (target == cur) {
            res.push_back(path);
            return;
        }
        for (int i = begin; i < size; i++) {
            int sum = cur + candidates[i];
            if (sum > target) {
                break;
            }
            path.push_back(candidates[i]);
            dfs(candidates, i, size, path, res, sum, target);
            path.pop_back();
        }
    }
    // TODO: 还可以使用动态规划
    // ...
    
};
// int main() {
//     Solution s;
//     vector<int> nums;
//     nums.push_back(2);
//     nums.push_back(3);
//     nums.push_back(6);
//     nums.push_back(7);
//     vector<vector<int> > res = s.combinationSum(nums, 7);
//     for (int i = 0; i < res.size(); i++) {
//         for (int j = 0; j < res[i].size(); j++) {
//             printf("%d ", res[i][j]);
//         }
//         printf("\n");
//     }
// }
