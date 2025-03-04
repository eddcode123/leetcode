from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
        return pointer
               

# testcase

solution = Solution()

result  = solution.removeElement([0,1,2,2,3,0,4,2], 2)
print(result)