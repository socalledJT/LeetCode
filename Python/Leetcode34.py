class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums == Null:
            return [-1, -1]

        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)

        return [left, right]

    # If LeftBias = False, we look for the right most occurance of the target.
    def binarySearch(self, nums, target, leftBias):
        left, right = 0, len(nums) - 1
        index = -1

        while left <= r:
            midpoint = (left + right) // 2
            if target > nums[midpoint]:
                left = midpoint + 1
            elif target < nums[midpoint]:
                right = midpoint - 1
            else:
                index = midpoint
                if leftBias:
                    right = midpoint - 1
                else:
                    left = midpoint + 1
        return index