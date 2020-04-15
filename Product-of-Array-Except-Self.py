'''


Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        multiple=1
        count=0
        pos=-1
        result=[0]*len(nums) 
        for i in range(0,len(nums)):
            if nums[i]==0:
                count+=1
                pos=i
            else:
                multiple*=nums[i]
        if count>1:
            return result
        elif count==1:
            result[pos]=multiple
            return result
        for i in range(0,len(nums)):
            result[i]=multiple/nums[i]
        return result
