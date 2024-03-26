# https://leetcode.com/problems/smallest-number-in-infinite-set/

import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.priority_queue = []
        self.element_set = set()
        self.next_available = 1

    def popSmallest(self) -> int:
        if not self.element_set:
            self.next_available += 1
            return self.next_available - 1
        smallest = heapq.heappop(self.priority_queue)
        self.element_set.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.next_available and num not in self.element_set:
            self.element_set.add(num)
            heapq.heappush(self.priority_queue, num)

if __name__ == "__main__":
    smallestInfiniteSet = SmallestInfiniteSet()
    print(smallestInfiniteSet.addBack(2))   # Output: None
    print(smallestInfiniteSet.popSmallest())  # Output: 1
    print(smallestInfiniteSet.popSmallest())  # Output: 2
    print(smallestInfiniteSet.popSmallest())  # Output: 3
    print(smallestInfiniteSet.addBack(1))   # Output: None
    print(smallestInfiniteSet.popSmallest())  # Output: 1
    print(smallestInfiniteSet.popSmallest())  # Output: 4
    print(smallestInfiniteSet.popSmallest())  # Output: 5