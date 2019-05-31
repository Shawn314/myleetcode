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
/*
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
}*/
/*
伪代码如下：

1) 将当前结点初始化为列表的哑结点。
2) 将进位carry初始化为0
3) 将p和q分别初始化为列表l1和l2的头部
4) 遍历列表l1和l2直至到达它们的尾端。
    · 将x设置为p的值。如果p已经达到了l1的末尾，则将其值设为0.
    · 将y设置为q的值。如果q已经达到了l2的末尾，则将其值设置为0.
    · 设定sum = x + y + carry;
    · carry = sum / 10.
    · 创建一个数值为(sum % 10)的节点，并将其设置为当前结点的下一结点，然后将当前
    结点前进到下一个结点。
    · 同时，将p和q前进到下一个结点。
5) 检查carry = 1是否成立，若成立，则新增一个含有数字1的新节点。
6) 返回哑结点的下一个结点。
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* dummyHead = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummyHead->val = 0;
    dummyHead->next = NULL;
    struct ListNode* cur = dummyHead;
    int carry = 0;
    struct ListNode* p = l1;
    struct ListNode* q = l2;
    while (p != NULL || q != NULL) {
        int x = (p != NULL)?p->val:0;
        int y = (q != NULL)?q->val:0;
        int sum = x + y + carry;
        carry = sum / 10;
        cur->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        cur = cur->next;
        cur->next = NULL;
        cur->val = sum % 10;
        if (p != NULL)
            p = p->next;
        if (q != NULL) {
            q = q->next;
        }
    }
    if (carry == 1) {
        cur->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        cur = cur->next;
        cur->next = NULL;
        cur->val = 1;
    }
    return dummyHead->next;
}
