class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combis = []
        self.dfs(candidates,target,[],combis)
        return combis
        
    def dfs(self,candidates,target,path,combis):
        if target < 0:
            return
        if target == 0:
            path.sort()
            combis.append(path)
        
        for index in range(len(candidates)): 
            # This is the tricky part. By using candidates[index:] in the dfs, we avoid repetition.
            self.dfs(candidates[index:],target-candidates[index],path+[candidates[index]],combis)