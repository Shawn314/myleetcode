/*
 * @lc app=leetcode.cn id=2 lang=c
 *
 * [2] 两数相加
 *
 * https://leetcode-cn.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (34.09%)
 * Total Accepted:    128.9K
 * Total Submissions: 378K
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
 * 
 * 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
 * 
 * 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
 * 
 * 示例：
 * 
 * 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
 * 输出：7 -> 0 -> 8
 * 原因：342 + 465 = 807
 * 
 * 
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* tmp1 = l1;
    struct ListNode* tmp2 = l2;
    bool carry = false;
    struct ListNode* l3 = (struct ListNode*)malloc(sizeof(struct ListNode));
    l3->val = 0;
    l3->next = NULL;
    struct ListNode* tmp3 = l3;
    int val;
    while (tmp1 != NULL && tmp2 != NULL) {
        if (carry) {
            val = tmp1->val + tmp2->val + 1;
        }else {
            val = tmp1->val + tmp2->val;
        }
        carry = false;
        if (val / 10 > 0) {
            val %= 10;
            carry = true;
        }
        tmp1 = tmp1->next;
        tmp2 = tmp2->next;
        struct ListNode* new_node;
        if (tmp1 && tmp2) {
            new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
            new_node->val = 0;
            new_node->next = NULL;
        }else {
            new_node = NULL;
        }
        tmp3->next = new_node;
        tmp3->val = val;
        if (new_node != NULL) {
            tmp3 = new_node;
        }
    }
    struct ListNode* new_node;
    if (tmp1 != NULL && tmp2 == NULL) {
        while (tmp1 != NULL) {
            new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
            new_node->val = 0;
            new_node->next = NULL;
            tmp3->next = new_node;
            tmp3 = new_node;
            
            if (carry) {
                carry = false;
                tmp3->val = tmp1->val+1;
                if (tmp3->val / 10 > 0){
                    tmp3->val %= 10;
                    carry = true;
                }
            }else {
                tmp3->val = tmp1->val;
            }
            tmp1 = tmp1->next;
        }
    }else if (tmp1 == NULL && tmp2 != NULL) {
        while (tmp2 != NULL) {
            
            new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
            new_node->val = 0;
            new_node->next = NULL;
            tmp3->next = new_node;
            tmp3 = new_node;
            
            if (carry) {
                carry = false;
                tmp3->val = tmp2->val+1;
                if (tmp3->val / 10 > 0){
                    tmp3->val %= 10;
                    carry = true;
                }
            }else {
                tmp3->val = tmp2->val;
            }
            tmp2 = tmp2->next;
        }
    }
    while (carry) {
        new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val = 0;
        new_node->next = NULL;
        tmp3->next = new_node;
        tmp3 = new_node;
        if ((tmp3->val + 1) / 10 > 0){
            tmp3->val++;
            tmp3->val %= 10;
            carry = true;
        }else {
            tmp3->val += 1;
            carry = false;
        }
    }
    return l3;
}



