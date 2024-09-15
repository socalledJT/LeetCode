# Generate Parentheses

"""
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]

Constraints:
    1 <= n <= 8

Base cases:
    n == 1:
        - The only valid combination is "()".

"""

class Solution:
    def generateParentheses(self, n: int) -> list[str]:
        # Generate a helper recursive function
        def helper(s, left, right):
            # Base case: if the length of the string is 2 * n, add it to the result list
            if len(s) == n * 2:
                result.append(s)
                return

            # If left value < n add a ( to the string, and add +1 to left
            if left < n:
                helper(s + "(", left + 1, right)
            # If right value < left value, add a ) to the string, and add +1
            if right < left:
                helper(s + ")", left, right + 1)


        result = []
        helper("", 0, 0)
        return result

# Testing
n = int(input("Enter num: "))
solution = Solution()
print(solution.generateParentheses(n))  # Output: ["((()))","(()())","(())
