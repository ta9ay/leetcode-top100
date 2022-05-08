# Divide and conquer
# Runtime 147ms 
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        
        return self.mergefunc(l,r)
            
        
    def mergefunc(self,left,right):
        head = curr = ListNode()
        
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
                curr = curr.next
            else:
                curr.next = right
                right = right.next
                curr = curr.next
        
        curr.next = left or right
        
        return head.next