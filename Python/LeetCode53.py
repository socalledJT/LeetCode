class Solution:
    def maxSubArray(self, nums):
        # Helper function that uses divide and conquer to find the maximum subarray sum
        def maxSubArray(A, L, R):
            # Base case: if L > R, the range is invalid, return negative infinity
            if L > R: 
                return float('-inf')
            
            # Find the middle index
            mid = (L + R) // 2
            
            # Initialize variables for the left and right subarrays and current sums
            left_sum, right_sum, cur_sum = 0, 0, 0
            
            # Calculate the maximum sum for the left half, ending at mid-1
            # We go backwards from the middle to the left side
            for i in range(mid - 1, L - 1, -1):
                # Add current element to cur_sum and update left_sum to be the max of itself and cur_sum
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            
            # Reset cur_sum for the right half calculation
            cur_sum = 0
            
            # Calculate the maximum sum for the right half, starting at mid + 1
            # We go forwards from the middle to the right side
            for i in range(mid + 1, R + 1):
                # Add current element to cur_sum and update right_sum to be the max of itself and cur_sum
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])
            
            # The maximum subarray sum could be in one of three places:
            # 1. The left half (recursively computed)
            # 2. The right half (recursively computed)
            # 3. The middle subarray that crosses the midpoint
            # The middle subarray includes the middle element, left_sum, and right_sum
            return max(
                maxSubArray(A, L, mid - 1),  # Maximum subarray sum in the left half
                maxSubArray(A, mid + 1, R),  # Maximum subarray sum in the right half
                left_sum + A[mid] + right_sum  # Maximum subarray sum crossing the middle
            )
        
        # Call the helper function on the entire array (from index 0 to len(nums) - 1)
        return maxSubArray(nums, 0, len(nums) - 1)
