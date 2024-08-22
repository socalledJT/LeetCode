class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Recursive function to break down the x^n formula
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            # Function will recursively call itself, using half of the n value to calculate the result
            result = helper(x, n // 2)
            # Then it will multiply the result to get the final value
            result = result * result
            # This takes care to see if the value of n was an odd number, by multiplying x to the result if so
            return x * result if n % 2 else result
        
        # The final result here takes the value from the helper function
        result = helper(x, abs(n))
        # If n was positive, the result is printed, if not 1 / result is printed instead
        return result if n >= 0 else 1 / result