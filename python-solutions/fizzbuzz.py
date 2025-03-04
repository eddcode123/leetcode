from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Generates a list of strings representing the FizzBuzz sequence up to `n`.

        For each integer from 1 to `n`:
        - If the number is divisible by 3 and 5, add "FizzBuzz" to the list.
        - If the number is divisible by 3, add "Fizz" to the list.
        - If the number is divisible by 5, add "Buzz" to the list.
        - Otherwise, add the number itself as a string.

        Args:
            n (int): The upper limit of the sequence (inclusive).

        Returns:
            List[str]: A list of strings representing the FizzBuzz sequence.

        Example:
            >>> solution = Solution()
            >>> solution.fizzBuzz(5)
            ['1', '2', 'Fizz', '4', 'Buzz']
        """

        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        
        return result
    
# test

solution = Solution()
result = solution.fizzBuzz(15)
print(result)