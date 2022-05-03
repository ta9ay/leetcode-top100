# runtime 25 ms
# Faster than 70.3% 
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # n,n stacks
        left = right = n
        result = []
        self.dfs(left,right,result,"")
        
        return result
        
    def dfs(self,left,right,result,current):
        
        if left > right:
            return
        
        if left == 0 and right == 0:
            result.append(current)
            return
            
        if left and left-1 <= right:
            self.dfs(left-1,right,result,current+"(")
        if right and right-1 >= left:
            self.dfs(left,right-1,result,current+")")