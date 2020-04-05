'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Code Explanation: the first stock is bought and if the next array element is greater than the the cost price of the stock cp
then it is sold when the stock is sold the profit is calculated.
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cp=0
        profit=0
        flag=0
        
        for i in range(0,len(prices)-1):
            if flag==0 and prices[i]<prices[i+1]:
                cp=prices[i]
                flag=1
            
            elif flag==1 and cp<prices[i] and prices[i]>prices[i+1]:
                #sp=prices[i]
                profit=profit+prices[i]-cp
                cp=0
                flag=0
                
        if flag==1 and prices[len(prices)-1]>cp:
            profit=profit+prices[len(prices)-1]-cp
            
        return profit   
