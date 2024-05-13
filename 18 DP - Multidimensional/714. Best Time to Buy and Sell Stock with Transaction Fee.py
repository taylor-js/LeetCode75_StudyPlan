# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0  # Max profit we can achieve without currently holding a stock
        hold = -prices[0]  # Max profit we can achieve while holding a stock
        
        for price in prices[1:]:
            old_cash = cash
            cash = max(cash, hold + price - fee)  # Sell stock
            hold = max(hold, old_cash - price)  # Buy stock
        
        return cash  # At the end, we want to end up without any stocks
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    mp1 = s.maxProfit([1, 3, 2, 8, 4, 9], 2)
    print(mp1)  # Output: 8
    # Example 2
    mp2 = s.maxProfit([1, 3, 7, 5, 10, 3], 3)
    print(mp2)  # Output: 6