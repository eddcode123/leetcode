from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Buy stock when at the lowest price and sell
        at highest price

        Args:
            prices (List(integers)): list of integers

        Returns:
            int: profit made or zero if not profit
                    can be made
        
        Example:
            >>> solution = Solution()
            >>> result = solution.maxprofit([7,1,5,3,6,4])
            >>> print(result)
            5
        """
        today, most_profitable = 0, 0

        for tomorrow in range(1, len(prices)):
            # check if selling at a loss
            if prices[tomorrow] - prices[today] <= 0:
                # skip buying stock that day
                today += 1
            # case where tomorrow has a better buying price
            if prices[today] > prices[tomorrow]:
                today = tomorrow
            else:
                if prices[tomorrow] - prices[today] > most_profitable:
                    most_profitable = prices[tomorrow] - prices[today]
        
        return most_profitable



    

# test case
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
