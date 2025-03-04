from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Calculates the maximum wealth among all customers.

        Each customer's wealth is calculated as the sum of money 
        in all their bank accounts. The function returns the 
        highest wealth value among all customers.

        Args:
            accounts (List[List[int]]): A 2D list where each sublist 
                represents the balances in all bank accounts of a 
                single customer.

        Returns:
            int: The maximum wealth among all customers.

        Example:
            >>> solution = Solution()
            >>> solution.maximumWealth([[1, 2, 3], [3, 2, 1], [4, 5, 6]])
            15
        """

        total_sum = []

        for customer in accounts:
            total_sum.append(sum(customer))
        
        return max(*total_sum)
