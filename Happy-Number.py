'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Explanation: We use an array #to keep track if a number is repeated or not if a number repeats then
there is an infinite loop hence it will never result in 1 and will go on
'''


class Solution(object):
    def sumSquares(self,n):
        sum=0
        while(n>0):
            sum=sum+pow(n%10,2)
            n=n//10
        return sum
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited=[]  
        while(n>1 and n not in visited):  
            visited.append(n)
            n=self.sumSquares(n)
        
        return n==1
