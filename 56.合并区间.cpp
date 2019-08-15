/*
 * @lc app=leetcode.cn id=56 lang=cpp
 *
 * [56] 合并区间
 *
 * https://leetcode-cn.com/problems/merge-intervals/description/
 *
 * algorithms
 * Medium (37.58%)
 * Total Accepted:    22.6K
 * Total Submissions: 59.9K
 * Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
 *
 * 给出一个区间的集合，请合并所有重叠的区间。
 * 
 * 示例 1:
 * 
 * 输入: [[1,3],[2,6],[8,10],[15,18]]
 * 输出: [[1,6],[8,10],[15,18]]
 * 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
 * 
 * 
 * 示例 2:
 * 
 * 输入: [[1,4],[4,5]]
 * 输出: [[1,5]]
 * 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
 * 
 */
#include <vector>
using namespace std;
class Solution {
public:
    static bool compare(vector<int>& a, vector<int>& b) {
        return (a[0] < b[0]);
    }
    /*
      关键点在于intervals[i][0]和intervals[i+1][1]的判断，
      1）若intervals[i][0]>intervals[i+1][1]，则两个区间有重叠，此时取 res.back()[1]
      中和intervals[i+1][1]中最大的值；
      2）若小于，则直接将区间 push 到 res 中。
    */
    vector<vector<int> > merge(vector<vector<int> >& intervals) {
        vector<vector<int> > res;
        if (intervals.empty()) {
            return res;
        }
        vector<int> range;
        sort(intervals.begin(), intervals.end(), compare);
        res.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); i++) {
            if (res.back()[1] < intervals[i][0]) {
                res.push_back(intervals[i]);
            }else {
                res.back()[1] = max(res.back()[1], intervals[i][1]);
            }
        }
        return res;
    }
};
// int main() {
//     Solution s;
//     vector<int> nums;
//     vector<vector<int> > intervals;
//     nums.push_back(9);
//     nums.push_back(13);
//     intervals.push_back(nums);
//     nums.clear();
//     nums.push_back(4);
//     nums.push_back(5);
//     intervals.push_back(nums);
//     nums.clear();
//     nums.push_back(1);
//     nums.push_back(8);
//     intervals.push_back(nums);
//     vector<vector<int> > res = s.merge(intervals);

// }
