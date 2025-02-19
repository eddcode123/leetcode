from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determines if you can reach the last index of the array.

        Args:
            nums (List[int]): List where each element represents the maximum jump length at that position.
        
        Returns:
            bool: True if you can reach the end of the array, otherwise False.
        
        Example:
            >>> solution = Solution()
            >>> result = solution.canJump([2, 3, 1, 1, 4])
            >>> print(result)
            True
            >>> result = solution.canJump([3, 2, 1, 0, 4])
            >>> print(result)
            False
           bool: True if you reach the end of the array else false
        """
        # Edge case: Single element array, no need to jump
        if len(nums) == 1:
            return True
        
        goal = len(nums) - 1  # Target index to reach
        
        for i in range(len(nums) - 2, -1, -1):  # Traverse from second last to the start
            # Check if the current index can reach or surpass the goal
            if i + nums[i] >= goal:
                goal = i  # Update the goal to the current index
        
        # If goal is at the start, return True
        return goal == 0
# testcase
solution = Solution()
print(solution.canJump([1]))