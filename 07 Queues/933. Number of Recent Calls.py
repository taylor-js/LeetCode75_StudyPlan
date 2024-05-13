# https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75

from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
    
if __name__ == "__main__":
    recentCounter = RecentCounter()
    # Example 1
    result = []
    rc1 = recentCounter.ping(1)
    rc2 = recentCounter.ping(100)
    rc3 = recentCounter.ping(3001)
    rc4 = recentCounter.ping(3002)
    result.append(rc1)
    result.append(rc2)
    result.append(rc3)
    result.append(rc4)
    print(result)