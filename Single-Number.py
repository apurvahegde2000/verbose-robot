'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

#Solution1
'''
Explanation:collections.Counter() gives the frequency of elements in an array in a dictionary format
if arr=[2,2,4,5,5,5]
   counter={2:2,4:1,5:3}
'''
import collections
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter=collections.Counter(nums) 
        
        for k,v in counter.items():
            if(v==1):
                return k
#Solution 2
'''
Explanation:here we used XOR operator
1.) a^a=0
2.) a^0=a
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        
        for i in nums:
            a^=i
        return a 
