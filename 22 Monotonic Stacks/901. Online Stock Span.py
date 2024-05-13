# https://leetcode.com/problems/online-stock-span/?envType=study-plan-v2&envId=leetcode-75

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        # Pop elements from the stack while the stack is not empty and the current price is greater or equal to the top of the stack's price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        # Push current price and its calculated span to the stack
        self.stack.append((price, span))
        return span

if __name__ == "__main__":
    # Example
    stockSpanner = StockSpanner()
    print(stockSpanner.next(100)) # Output: 1
    print(stockSpanner.next(80)) # Output: 1
    print(stockSpanner.next(60)) # Output: 1
    print(stockSpanner.next(70)) # Output: 2
    print(stockSpanner.next(60)) # Output: 1
    print(stockSpanner.next(75)) # Output: 4
    print(stockSpanner.next(85)) # Output: 6