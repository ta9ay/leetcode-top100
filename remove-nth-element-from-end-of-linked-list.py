# runtime 35 ms
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        if not head:
            return []
        
        # count length
    
        length = self.getlength(head)
        
        
        # get last nth
        if length < n:
            return head
        
        curr = head
        if length == n:
            #remove first node
            head = curr.next
            return head

        for i in range(0,(length-n)-1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head
        
        
        
        
    def getlength(self,head):
        count = 0
        while head:
            count += 1
            head = head.next
        
        return count