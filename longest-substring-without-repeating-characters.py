# runtime: 37 ms

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = max_length = 0
        seen = {}

        for index,c in enumerate(s):
            if c in seen and head <= seen[c]:
                head = seen[c] + 1

            else:
                max_length = max(max_length, index - head + 1)
            
            seen[c] = index

        return max_length

