# runtime 20ms
# Faster than 69.97%

class Solution(object):
    mapping = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
            '0':[' ']
            
        }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == "":
            return []
            
        combination = ['']
        for digit in digits:
            combination = self.getcombination(combination,digit)
        
        return combination
        
    def getcombination(self,combination,num):
        result = (p + q for p in combination for q in self.mapping[num])
        
        return result
    