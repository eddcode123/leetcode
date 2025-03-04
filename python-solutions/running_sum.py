from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Computes the running sum of a list of integers.

        The running sum is a new array where each element at index `i` is the 
        sum of all elements from index `0` to `i` in the input list. The operation 
        is performed in-place, modifying the original list.

        Args:
            nums (List[int]): A list of integers for which the running sum is to be calculated.
        
        Returns:
            List[int]: The input list updated with its running sum values.

        Example:
            >>> solution = Solution()
            >>> solution.runningSum([1, 2, 3, 4])
            [1, 3, 6, 10]
        """

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        return nums
