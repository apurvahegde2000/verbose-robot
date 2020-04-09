'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

The number of nodes in the given list will be between 1 and 100.

Explanation:We use 2 pointers one fast and one slow pointer to find the middle element
How to find middle element of Linked List in Single Pass ?
Solution : Start two pointer one will go two node ahead and the other will go one when
the faster one reaches end the slower one will be in the middle.
'''
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
    ListNode *p1=head;
    ListNode *p2=head;
    while(p2!=NULL && p2->next!=NULL)
    {
        
        p1=p1->next;
        p2=p2->next->next;
    }
    
    return p1;
        
    }
};
