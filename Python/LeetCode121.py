class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1 # Initialize two pointers to check each price in the array
        max_profit = 0 # To store the maximum profit

        while sell < len(prices): # Iterate through the array to check prices
            if prices[buy] < prices[sell]:  # If we have found a low buy price
                current_profit = prices[sell] - prices[buy] # caluclate the current profit for the 2 prices
                max_profit = max(max_profit, current_profit)    # If the current profit is bigger than the previous one make that the new maximum profit
            else: # If not
                buy = sell  # Move the buy position to the right, since the sell position is lower
            sell += 1 # Move the sell position to the right to iterate rhough the array
        
        return max_profit # Return the final profit
