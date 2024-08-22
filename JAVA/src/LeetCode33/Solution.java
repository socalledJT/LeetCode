package LeetCode33;
class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1;

        int start = 0;
        int end = nums.length - 1;

        // Find out where the pivot is
        while (start < end) {
            int midpoint = start + (end - start) /2;

            if (nums[midpoint] > nums[end]) {
                start = midpoint + 1;
            } else {
                end = midpoint;
            }
        }
        
        // Set the sorted array start to the start value (0)
        int arrayStart = start;
        start = 0;
        end = nums.length - 1;

        if (target >= nums[arrayStart] && target <= nums[end]) {
            start = arrayStart;
        } else {
            end = arrayStart;
        }

        // Binary search to find target
        while (start <= end) {
            int midpoint = start + (end - start) / 2;

            if (nums[midpoint] == target) {
                return midpoint;
            } else if (nums[midpoint] < target) {
                start = midpoint + 1;
            } else {
                end = midpoint - 1;
            }
        }

        return -1;
    }
}