/*
 * @lc app=leetcode.cn id=40 lang=cpp
 *
 * [40] 组合总和 II
 *
 * https://leetcode-cn.com/problems/combination-sum-ii/description/
 *
 * algorithms
 * Medium (56.16%)
 * Total Accepted:    18.4K
 * Total Submissions: 32.7K
 * Testcase Example:  '[10,1,2,7,6,1,5]\n8'
 *
 * 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
 * 
 * candidates 中的每个数字在每个组合中只能使用一次。
 * 
 * 说明：
 * 
 * 
 * 所有数字（包括目标数）都是正整数。
 * 解集不能包含重复的组合。 
 * 
 * 
 * 示例 1:
 * 
 * 输入: candidates = [10,1,2,7,6,1,5], target = 8,
 * 所求解集为:
 * [
 * ⁠ [1, 7],
 * ⁠ [1, 2, 5],
 * ⁠ [2, 6],
 * ⁠ [1, 1, 6]
 * ]
 * 
 * 
 * 示例 2:
 * 
 * 输入: candidates = [2,5,2,1,2], target = 5,
 * 所求解集为:
 * [
 * [1,2,2],
 * [5]
 * ]
 * 
 */
#include <vector>
using namespace std;

class Solution {
public:
    /*
      思路：回溯，画树图
      关键点：和39题相比，多了一个条件就是每个数字在每个解集中只能用一次(暗示排
      序)，因为相同的元素第一个元素会包含所有的解集，所以后面的就可以跳过了。
     */
    vector<vector<int> > combinationSum2(vector<int>& candidates, int target) {
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
    void dfs(vector<int>& candidates, int start, int size, vector<int>& path, vector<vector<int> >& res, int target) {
        if (target == 0) {
            res.push_back(path);
            return;
        }
        for (int i = start; i < size; i++) {
            if (i > start && candidates[i-1] == candidates[i]) {
                continue;
            }
            int remain = target - candidates[i];
            if (remain < 0) {
                continue;
            }
            path.push_back(candidates[i]);
            dfs(candidates, i+1, size, path, res, remain);
            path.pop_back();
        }
    }
};
// int main() {
//     Solution s;
//     vector<int> nums;
//     nums.push_back(10);
//     nums.push_back(1);
//     nums.push_back(2);
//     nums.push_back(7);
//     nums.push_back(6);
//     nums.push_back(1);
//     nums.push_back(5);
//     vector<vector<int> > res = s.combinationSum2(nums, 8);
//     for (int i = 0; i < res.size(); i++) {
//         for (int j = 0; j < res[i].size(); j++) {
//             printf("%d ", res[i][j]);
//         }
//         printf("\n");
//     }
// }
