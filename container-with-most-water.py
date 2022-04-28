# runtime: 516ms
# faster than 99.26% Python solutions
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        first = 0
        last = len(height) - 1
        
        curr_area = max_area = 0
        
        while last > first:
            smaller_height = min(height[first],height[last])
            curr_area = abs(first-last)*smaller_height
            max_area = max(max_area,curr_area)
            if height[first] < height[last]:
                first+=1
                while height[first] < smaller_height:
                    first+=1
            else:
                last -= 1
                while height[last] < smaller_height:
                    last-=1
        return max_area