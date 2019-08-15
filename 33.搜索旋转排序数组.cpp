/*
 * @lc app=leetcode.cn id=33 lang=cpp
 *
 * [33] 搜索旋转排序数组
 *
 * https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
 *
 * algorithms
 * Medium (36.09%)
 * Total Accepted:    34.6K
 * Total Submissions: 95.9K
 * Testcase Example:  '[4,5,6,7,0,1,2]\n0'
 *
 * 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
 * 
 * ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
 * 
 * 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
 * 
 * 你可以假设数组中不存在重复的元素。
 * 
 * 你的算法时间复杂度必须是 O(log n) 级别。
 * 
 * 示例 1:
 * 
 * 输入: nums = [4,5,6,7,0,1,2], target = 0
 * 输出: 4
 * 
 * 
 * 示例 2:
 * 
 * 输入: nums = [4,5,6,7,0,1,2], target = 3
 * 输出: -1
 * 
 */
/*
  思路：二分搜索，有序区间的确认是通过中间点和最右边的点来确定的。
        1）若中间点小于最右边值，则右边界有序，如果此时 target 正好再次区间继续用二
        分；
        2）若中间点大于最右边值，则左边界有序；
        3）若进入无序区间，则是一半有序一半无序。
 */
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int length = nums.size();
        if (length <= 0) {
            return -1;
        }
        int lo = 0;
        int hi = length - 1;
        while (lo <= hi) {
            int mid = lo + ((hi - lo)>> 1);
            if (target == nums[mid]) {
                return mid;
            }
            //右侧有序
            if (nums[mid] < nums[hi]) {
                if (target > nums[mid] && target <= nums[hi]) {
                    lo = mid + 1;
                }else {
                    hi = mid - 1;
                }
            }else{
                //左侧有序
                if (target < nums[mid] && target >= nums[lo]) {
                    hi = mid - 1;
                }else {
                    lo = mid + 1;
                }
            }
        }
        return -1;
    }
};
 
