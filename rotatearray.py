from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array to the right by k steps in-place.

        Args:
            nums (List[int]): List of integers to rotate.
            k (int): Number of positions to rotate.

        Example:
            >>> nums = [1, 2, 3, 4, 5, 6]
            >>> solution = Solution()
            >>> solution.rotate(nums, 3)
            >>> print(nums)
            [4, 5, 6, 1, 2, 3]
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums

# test case
solution = Solution()

print(solution.rotate([1, 2, 3, 4, 5, 6], 3))