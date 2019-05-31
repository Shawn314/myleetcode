/*
 * @lc app=leetcode.cn id=1 lang=c
 *
 * [1] 两数之和
 *
 * https://leetcode-cn.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (45.94%)
 * Total Accepted:    385.1K
 * Total Submissions: 836.5K
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
 * 
 * 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
 * 
 * 示例:
 * 
 * 给定 nums = [2, 7, 11, 15], target = 9
 * 
 * 因为 nums[0] + nums[1] = 2 + 7 = 9
 * 所以返回 [0, 1]
 * 
 * 
 */


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdlib.h>
#include <string.h>
#include <math.h>
//first: Profiteering solution, o(n2)
/*int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* index = (int*)malloc(sizeof(int) * 2);
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                index[0] = i;
                index[1] = j;
                *returnSize = 2;
                return index; 
            }
        }
    }
    return NULL;
}
*/
//second: hash table, time o(1)

typedef struct node_st {
    int key;
    int val;
    struct node_st* next;
}*node_t;

typedef struct map_st {
    node_t* nodeArr;
    size_t size;
}*map_t;

map_t createMap(int table_size) {
    map_t map = (map_t)malloc(sizeof(struct map_st) * 1);
    map->size = table_size;
    map->nodeArr = (node_t*)malloc(sizeof(node_t) * table_size);
    memset(map->nodeArr, 0, sizeof(node_t) * table_size);
    return map;
}
int getHashCode(map_t map, int key) {
    return abs(key) % map->size;
}
void add(map_t map, int key, int val) {
    int hash_id = getHashCode(map, key);
    node_t tmp_node = map->nodeArr[hash_id];
    while (tmp_node != NULL) {
        if (tmp_node->key == key) {
            return;
        }
        tmp_node = tmp_node->next;
    }
    tmp_node = map->nodeArr[hash_id];
    node_t new_node = (node_t)malloc(sizeof(struct node_st) * 1);
    new_node->key = key;
    new_node->val = val;
    new_node->next = tmp_node;
    map->nodeArr[hash_id] = new_node;
}
int find(map_t map, int key) {
    int hash_id = getHashCode(map, key);
    node_t tmp_node = map->nodeArr[hash_id];
    while (tmp_node != NULL) {
        if (tmp_node->key == key){
            return tmp_node->val;
        }
        tmp_node = tmp_node->next;
    }
    return -1;
}



int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    map_t map = createMap(numsSize);
    int* index = (int*)malloc(sizeof(int) * 2);
    for (int i = 0; i < numsSize; i++) {
         int key = target - nums[i];
         int val = -1;
         if ((val = find(map, key)) != -1) {
             index[0] = val;
             index[1] = i;
             *returnSize = 2;
             return index;
         }else {
             add(map, nums[i], i);
         }
    }
    return NULL;
}

