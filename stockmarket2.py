from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit you can make from multiple stock transactions.
        
        Args:
            prices (List[int]): List of daily stock prices.
        
        Returns:
            int: Total profit from all profitable transactions.
        
        Example:
            >>> solution = Solution()
            >>> result = solution.maxProfit([7,1,5,3,6,4])
            >>> print(result)
            7
        """
        total_profit = 0
        today = 0

        for tomorrow in range(1, len(prices)):
            # Calculate the potential profit for the day
            profit = prices[tomorrow] - prices[today]

            if profit > 0:
                # Add to the total profit if it's profitable
                total_profit += profit
                # Move to the next day after selling
                today += 1
            else:
                # Move to the next day if no profit is possible
                today = tomorrow
        
        return total_profit


# test case
solution = Solution()
print(solution.maxProfit([7,6,4,3,1]))