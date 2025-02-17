from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ Remove some duplicate in-place such that
        each unique element only appears twice at most

        Args:
            nums (List[int]): list of integers

        Returns:
            int: the first n unique elements that appear atleast twice

        Example:
            >>> solution = Solution()
            >>> result = solution.removeDuplicates([1,1,1,2,2,3])
            >>> print(result)
            5 [1,1,2,2,3,1]
        """

        # edge case

        insert_pos = 1
        count = 1
        max_occurrence = 2

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
        
            if count <= max_occurrence:
                if insert_pos != i:
                    nums[insert_pos] = nums[i]
                insert_pos += 1
        
        return insert_pos

    
# testcase
solution = Solution()

print(solution.removeDuplicates([0,0,1,1,1,1,2,3,3]))

            
