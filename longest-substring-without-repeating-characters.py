# runtime:

class Solution:
    def lengthOfLongestSubstring(self,s):
        head = max_length = 0
        seen = {}

        for index,c in enumerate(s):
            if c in seen and head <= seen[c]:
                start = used[c] + 1

            else:
                max_length = max(max_length, i - start + 1)
                seen[c] = i

        return max_length

