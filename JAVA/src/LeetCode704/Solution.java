package LeetCode704;

public class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int midPoint = (left + right) / 2;
            
            if (nums[midPoint] > target) {
                right = midPoint - 1;
            }
            else if (nums[midPoint] < target) {
                left = midPoint + 1;
            }
            else {
                return midPoint;
            }
        }
        return -1;
    }
}
