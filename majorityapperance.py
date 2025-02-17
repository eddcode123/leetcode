from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """ Return the element that appears more than
        n/2 where n is size of nums
        
        Args:
            nums (List(int : list of integers
        
        Returns:
            int : element that appears most times
        
        Example:
            >>> solution = Solution()
            >>> result = solution.majorityElement([2,2,1,1,1,2,2])
            >>> print(result)
            2
        """
        res, count = 0, 0

        for num in nums:
            if count == 0:
                res = num
            
            count += (1 if num == res else -1)
        
        return res
        


# testcase
solution = Solution()
result = solution.majorityElement([2,2,1,1,1,2,2])
print(result)