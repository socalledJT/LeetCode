class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Sort the array
        nums.sort()
        res = []

        # Iterate through the array
        for i in range(len(nums) - 2):
            # Skip the same `nums[i]` to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers to find the two other numbers
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    # Found a triplet
                    res.append([nums[i], nums[left], nums[right]])
                    # Move both pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return res
