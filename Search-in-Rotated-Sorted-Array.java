/**


33. Search in Rotated Sorted Array
Description
Hints
Submissions
Discuss
Solution
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
/

//Solution 1: BRUTE FORCE METHOD (time=1ms) 
class Solution {
    public int search(int[] nums, int target) {
        int r,i;
        for(i=0;i<nums.length;i++)
        {
            if(nums[i]==target) 
                return i;
        }
        return -1;
    }
}

//Solution 2: QUICK SORT METHOD (time=1ms) 
class Solution {
    int partition(int[] A,int l,int h) 
    {
        int p=l,i=l+1,j=h;
        do
        {
            while(i<h && A[p]>=A[i]) 
                i++;
            while(j>l && A[p]<A[j]) 
                j--;
            if(i<j) 
            {
                int t=A[i];
                A[i]=A[j];
                A[j]=t;
            }
        }while(i<j);
        int t=A[p];
        A[p]=A[j];
        A[j]=t;
        return j;
    }
    public int search(int[] nums, int target) {
        int s, e;
        int l=nums.length;
        if(l==0) return -1;
        if(target==nums[0]) 
           return 0;
        int[] a=nums.clone();
        int p=partition(a,0,l-1);
        if(target<nums[0]) 
        {s=l-p;e=l-1;}
        else
        {s=0;e=l-p-1;}
        for(int i=s;i<=e;i++) 
        {
            if(target==nums[i]) 
                return i;
        }
        return -1;
    }
}
