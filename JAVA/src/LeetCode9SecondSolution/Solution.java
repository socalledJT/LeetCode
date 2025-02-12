package LeetCode9SecondSolution;

public class Solution {
    public boolean isPalindrome(int x) {
        // Negative Numbers are always false
        if (x < 0) {
            return false;
        }

        int lVal = 1;
        while (x >= 10 * lVal) {
            // Var to calculate the value of the left digit of the integer
            // 121 would % by 100 for us to get the left 1 digit on the hundreds
            lVal *= 10;
        }

        while ( x != 0) {
            // Find the right digit
            int right = x % 10;
            // Find the left Digit
            int left = x / lVal;

            // Compare the two digits to see if they are a palindrome
            if (left != right) {
                return false;
            }
            // Chop off the two left and right digits
            x = (x % lVal) / 10;
            // Remove two digits from the lVal calculator since we removed 2 digits from the integer
            lVal = lVal / 100;
        }
        return true;
    }
}
