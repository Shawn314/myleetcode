/*
 * @lc app=leetcode.cn id=78 lang=cpp
 *
 * [78] 子集
 *
 * https://leetcode-cn.com/problems/subsets/description/
 *
 * algorithms
 * Medium (74.28%)
 * Total Accepted:    30.1K
 * Total Submissions: 40.4K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
 * 
 * 说明：解集不能包含重复的子集。
 * 
 * 示例:
 * 
 * 输入: nums = [1,2,3]
 * 输出:
 * [
 * ⁠ [3],
 * [1],
 * [2],
 * [1,2,3],
 * [1,3],
 * [2,3],
 * [1,2],
 * []
 * ]
 * 
 */
#include <vector>
#include <stdio.h>
using namespace std;
class Solution {
public:
    /*
      Solution:回溯，画树图，看符合规则的路径如何放到结果中（叶子结点）。
     */
    vector<vector<int> > subsets(vector<int>& nums) {
        vector<vector<int> > res;
        int size = nums.size();
        if (size <= 0) {
            return res;
        }
        vector<int> path;
        backtrack2(nums, size, 0, path, res);
        return res;
    }
    /*
      自己写的回溯，回溯开始点从当前开始，其实从下一个开始即可
      还有一点是，这里不需要排序。
     */
    void backtrack1(vector<int>& nums, int size, int start, vector<int>& path, vector<vector<int> >& res) {
        // 可以精简，因为此结束条件亦为 for 循环的结束条件（注释掉）
        // if (start >= size) {
            // return;
        // }
        for (int i = start; i < size; i++) {
            if (!path.empty()){
                int last_val = -1;
                last_val = path.back();
                if (last_val == nums[i]) {
                    res.push_back(path);
                    continue;
                }
            }
            path.push_back(nums[i]);
            backtrack1(nums, size, i, path, res);
            path.pop_back();
        }
    }
    /*
      回溯：回溯的过程是执行一次深度优先遍历，一条路走到底，走不通的时候，
      返回回来，继续执行，一直这样下去，直到回到起点。
      经过分析，在根节点，非叶子节点，叶子结点都需要结算，所以开始下一次递
      归之前将路径保存到结果中;
     */
    void backtrack2(vector<int>& nums, int size, int start, vector<int>& path, vector<vector<int> >& res) {
        res.push_back(path);
        for (int i = start; i < size; ++i) {
            path.push_back(nums[i]);
            backtrack2(nums, size,i+1,path,res);
            path.pop_back();
        }
    }
    vector<vector<int> > subsets1(vector<int>& nums) {
        vector<vector<int> > res;
        int size = nums.size();
        if (size <= 0) {
            return res;
        }
        for (int i = 0; i <= size; i++) {
            vector<int> path;
            backtrack3(nums, size, i, 0, path, res);
        }
        return res;
    }
    void backtrack3(vector<int>& nums, int size, int depth, int start, vector<int>& path, vector<vector<int> >& res) {
        if (path.size() == depth){
            res.push_back(path);
            return;
        }
        for (int i = start; i < size; i++) {
            path.push_back(nums[i]);
            backtrack3(nums, size, depth, i+1,path, res);
            path.pop_back();
        }
    }
    /*
      方法是，读每个数字，然后将每个数字加入到当前结果的子集中。
     */
    vector<vector<int> > subsets2(vector<int>& nums) {
        vector<vector<int> > res;
        vector<int> tmp;
        res.push_back(tmp);
        for (int i = 0; i < nums.size(); i++) {
            int all = res.size();
            for (int j = 0; j < all; j++) {
                vector<int> tmp(res[j]);
                tmp.push_back(nums[i]);
                res.push_back(tmp);
            }
        }
        return res;
    }
    // 位运算法，如果数组中有三个元素，则所有组合都可以看成
    // 位，如000-111，组合的其中的位对应了数组的索引的位置，
    // 总得组合数目是2^3
    // 0: 0 0 0 ---> []
    // 1: 0 0 1 ---> nums[0]
    // 2: 0 1 0 ---> nums[1]
    // 3: 0 1 1 ---> nums[0] nums[1] 
    // 4: 1 0 0 ---> ...
    // 5: 1 0 1
    // 6: 1 1 0
    // 7: 1 1 1
    vector<vector<int> > subsets3(vector<int>& nums) {
        vector<vector<int> > res;
        int size = nums.size();
        if (size == 0) {
            return res;
        }
        int sum = 1 << size;
        for (int i = 0; i < sum; i++) {
            vector<int> vec;
            for (int j = 0; j < size; j++) {
                if ((i >> j) & 1) {
                    vec.push_back(nums[j]);
                }
            }
            res.push_back(vec);
        }
        return res;
    }
};
// int main() {
//     Solution s;
//     vector<int> nums;
//     nums.push_back(1);
//     nums.push_back(2);
//     nums.push_back(3);
//     vector<vector<int> > res = s.subsets(nums);
//     for (int i = 0; i < res.size(); i++) {
//         for (int j = 0; j < res[i].size(); j++) {
//             printf("%d ", res[i][j]);
//         }
//         printf("\n");
//     }
// }

