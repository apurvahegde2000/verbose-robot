'''
Given an integer array nums, find the "contiguous" subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
class Solution(object):
    
    def maxSubArray(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        max_so_far = a[0] 
        curr_max = a[0] 
      
        for i in range(1,len(a)): 
            curr_max = max(a[i], curr_max + a[i]) 
            max_so_far = max(max_so_far,curr_max) 
          
        return max_so_far    
        
