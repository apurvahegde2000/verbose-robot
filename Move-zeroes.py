'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations. 

Explanation:two pointer method is useful for such problems
where u need to do array manipulation without using extra space

'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(0,len(nums)) :
            if nums[j]!=0:
                nums[i]=nums[j]
                i=i+1
        if i!=len(nums):
            while i!=len(nums) :
                nums[i]=0
                i+=1
