class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* cur = head;
        int count = 0;
        if(head == NULL) return head;
        else{
            while(cur != NULL){
                cur = cur->next;
                count++;
            }
            cur = head;
            count = count/2;
            while(count--){
                cur = cur->next;
            }
        }
        return cur;
    }
};