class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNum = {} # Value : Index

        for i, n in enumerate(nums):    # Enumerate throgh the given array
            diff = target - n   # Divide the target by the current number, to find which number we need next
            if diff in prevNum: # If that number is found on the Dictionary,
                return [prevNum[diff], i]   # Return the index of that number, and of the current number
            else:   # If not
                prevNum[n] = i  # Add the current number to the Dictionary and move on
        return
