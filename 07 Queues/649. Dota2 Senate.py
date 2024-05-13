# https://leetcode.com/problems/dota2-senate/?envType=study-plan-v2&envId=leetcode-75

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D_queue, R_queue = deque(), deque()
        for i, c in enumerate(senate):
            if c == "R":
                R_queue.append(i)
            else:
                D_queue.append(i)
        while D_queue and R_queue:
            dTurn = D_queue.popleft()
            rTurn = R_queue.popleft()
            if rTurn < dTurn:
                R_queue.append(dTurn + len(senate))
            else:
                D_queue.append(rTurn + len(senate))
        return "Radiant" if R_queue else "Dire"
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    senate1 = "RD"
    ppv1 = s.predictPartyVictory(senate1)
    print(ppv1)
    # Example 2
    senate2 = "RDD"
    ppv2 = s.predictPartyVictory(senate2)
    print(ppv2)