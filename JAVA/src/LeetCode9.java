class Solution {
    public boolean isPalindrome(int x) {

        String temp = Integer.toString(x);
        int[] newX = new int[temp.length()];
        
        for (int i = 0; i < temp.length(); i++) {
            newX[i] = temp.charAt(i) - '0';
        }

        int i = 0;
        int j = temp.length() - 1;

        while (i < j) {
            if (newX[i] != newX[j]) {
                return false;
            }

            i++;
            j--;
        }

        return true;
    }
}
