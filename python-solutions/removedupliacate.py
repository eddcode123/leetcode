from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_pointer = 0

        if not nums:
            return 0

        for i in range(len(nums)):
            if nums[i] != nums[prev_pointer]:
                prev_pointer += 1
                nums[prev_pointer] = nums[i]
        return prev_pointer + 1




# testcase
solution = Solution()

print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))