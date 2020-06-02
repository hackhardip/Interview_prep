'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        '''        total = 0
        
        for i in range(1, len(height)-1):
            l_max = max(height[:i])
            r_max = max(height[i+1:])
            diff  = min(l_max, r_max)
            if diff-height[i] > 0:
                total = total + (diff-height[i])

        return total'''
        '''
        ans = 0
        for i in range(1,len(height)-1):
            l_max = max(height[:i])
            r_max = max(height[i+1:])
            diff = min(l_max,r_max)
            if diff-height[i] > 0:
                ans = ans + (diff-height[i])
        return ans
        '''
        left_max = 0
        right_max = 0
        left = 0
        right = len(height)-1
        ans=0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += (left_max-height[left])
                left+=1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max-height[right])
                right-=1
        return ans     
