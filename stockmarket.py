from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit from a single stock transaction.
        
        Args:
            prices (List[int]): List of daily stock prices.
        
        Returns:
            int: Maximum profit achievable, or 0 if no profit can be made.
        
        Example:
            >>> solution = Solution()
            >>> result = solution.maxProfit([7,1,5,3,6,4])
            >>> print(result)
            5
        """
        today = 0
        most_profitable = 0

        for tomorrow in range(1, len(prices)):
            # Check if selling at a loss
            if prices[tomorrow] - prices[today] <= 0:
                # Skip buying stock that day
                today += 1
            
            # Update the buying day if tomorrow offers a better price
            if prices[today] > prices[tomorrow]:
                today = tomorrow
            else:
                # Calculate profit and update if it's the most profitable so far
                profit = prices[tomorrow] - prices[today]
                if profit > most_profitable:
                    most_profitable = profit

        return most_profitable




    

# test case
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
