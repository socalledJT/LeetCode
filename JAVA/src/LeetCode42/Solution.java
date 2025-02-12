class Solution {
    public int trap(int[] height) {
        // Take into consideration that the array might be empty
        if (height == null || height.length == 0) {
            return 0;
        }
        
        // Create pointers to traverse array
        int left = 0;
        int right = height.length - 1;
        //F= Final result
        int res = 0;

        // Vars to hold the max values for calculations
        int leftMax = height[left];
        int rightMax = height[right];

        // While loop to traverse through the two pointers
        while (left < right) {
            // Start traversing based on the values of the max vars
            if (leftMax < rightMax) {
                // Iterate to the next value
                left += 1;
                // Update max if needed
                leftMax = Math.max(leftMax, height[left]);
                // Add the trapped water in the result
                res += leftMax - height[left];
            } else { // This ensures thta when Max values are equal there is still movement
                right -= 1;
                rightMax = Math.max(rightMax, height[right]);
                res += rightMax - height[right];
            }
        }
        // Return the result
        return res;
    }
}
