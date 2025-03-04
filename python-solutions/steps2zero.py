class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
        """
        # create a count varible to track the steps it took to get zero
        count = 0
        while (num > 0):
            # check if num  is even
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1
            
        return count


# test
solution = Solution()

result = solution.numberOfSteps(8)
print(result)