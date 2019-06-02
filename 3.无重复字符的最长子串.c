/*
 * @lc app=leetcode.cn id=3 lang=c
 *
 * [3] 无重复字符的最长子串
 *
 * https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (29.44%)
 * Total Accepted:    130K
 * Total Submissions: 438.7K
 * Testcase Example:  '"abcabcbb"'
 *
 * 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
 * 
 * 示例 1:
 * 
 * 输入: "abcabcbb"
 * 输出: 3 
 * 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 * 
 * 
 * 示例 2:
 * 
 * 输入: "bbbbb"
 * 输出: 1
 * 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
 * 
 * 
 * 示例 3:
 * 
 * 输入: "pwwkew"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
 * 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 * 
 * 
 */
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
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
void clear(map_t map) {
    for (int i = 0; i < map->size; i++) {
        node_t node_head = map->nodeArr[i];
        if (node_head == NULL) {
            continue;
        }
        while (node_head != NULL) {
            node_t node_next = node_head->next;
            free(node_head);
            node_head = node_next;
        }
        map->nodeArr[i] = NULL;
    }
}
void removeKey(map_t map, int key) {  
    int hash_id = getHashCode(map, key);
    node_t tmp = map->nodeArr[hash_id];
    node_t last_node = NULL;
    while (tmp != NULL) {
        if (tmp->key == key) {
            node_t next_node = tmp->next;
            if (last_node != NULL) {
                last_node->next = next_node;
            }else {
                map->nodeArr[hash_id] = next_node;
            }
            free(tmp);
            break;
        }
        last_node = tmp;
        tmp = tmp->next;
    }
}
void freeMap(map_t map) {
    if (map == NULL) {
        return;
    }
    for (size_t i = 0; i < map->size; i++) {
        if (map->nodeArr[i] != NULL) {
            free(map->nodeArr[i]);
        }
    }
    free(map->nodeArr);
    free(map);
}
// solution1: Profiteering solution, o(n2)
/*int lengthOfLongestSubstring(char * s){
    if (strlen(s) <= 1) {
        return strlen(s);
    }
    map_t map = createMap(strlen(s)*2);
    int largest_len = 0;
    for (size_t i = 0; i < strlen(s) - 1; i++){
        clear(map);
        add(map, s[i], i);
        for (size_t j = i + 1; j < strlen(s); j++) {
            if (find(map, s[j]) != -1) {
                if (j - i > largest_len){
                    largest_len = j - i;
                }
                break;
            }else {
                add(map, s[j], j);
                if (j - i >= largest_len) {
                    largest_len = j - i + 1;
                }
            }
        }
    }
    freeMap(map);
    return largest_len;
}*/

// solution2: sliding window(new)
/* int lengthOfLongestSubstring(char * s) { */
/*     int len = strlen(s); */
/*     map_t map = createMap(len);  */
/*     int i = 0, j = 0; */
/*     int largest_len = 0; */
/*     int j_pos; */
/*     while (i < len && j < len) { */
/*         if ((j_pos=find(map,s[j])) == -1) { */
/*             add(map,s[j], j); */
/*             j++; */
/*             largest_len = largest_len > (j - i)?largest_len:(j-i); */
/*         }else { */
/*             removeKey(map, s[j]); */
/*             i = i > (j_pos + 1)?i:(j_pos + 1); */
/*         } */
/*     } */
/*     return largest_len; */
/* } */
/*
## 这道题主要用到思路是：滑动窗口
   什么是滑动窗口？
   其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
   如何移动？
   我们只要把队列的左边的元素移出就行了，直到满足题目要求！
   一直维持这样的队列，找出队列出现最长的长度时候，求出解！
   时间复杂度：O(n)
*/


// solution3: optimized sliding window version.
int lengthOfLongestSubstring(char * s) {
    int len = strlen(s);
    map_t map = createMap(len); 
    int i = 0, j = 0;
    int largest_len = 0;
    int j_pos;
    while (i < len && j < len) {
        if ((j_pos=find(map,s[j])) == -1) {
            add(map,s[j], j);
            j++;
            largest_len = largest_len > (j - i)?largest_len:(j-i);
        }else {
            removeKey(map, s[j]);
            i = i > (j_pos + 1)?i:(j_pos + 1);
        }
    }
    return largest_len;
}

/* int main () { */
/*     char* s = "abba"; */
/*     printf("%d\n", lengthOfLongestSubstring(s)); */
/*     return 0; */
/* } */

