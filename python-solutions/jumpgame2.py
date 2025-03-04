from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Args:
            Args:
            nums (List[int]): List where each element
                    represents the maximum jump length at that position
            
            Returns:
                int: minimun number of jumpr required to n - 1

        '''
        goal = len(nums) - 1
        step = 0

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                step += 1
        
        return step

# test case

solution = Solution()
print(solution.jump([2,3,0,1,4]))