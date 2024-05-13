# https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap of size k
        heap = nums[:k]
        heapq.heapify(heap)
        
        # Iterate through the rest of the array
        for num in nums[k:]:
            # If the current number is greater than the smallest number in the heap,
            # replace the smallest number with the current number
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        # The root of the heap will be the kth largest element
        return heap[0]
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    nums1 = [3,2,1,5,6,4]
    k1 = 2
    fkl1 = s.findKthLargest(nums1,k1)
    print(fkl1)
    # Example 2
    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    fkl2 = s.findKthLargest(nums2, k2)
    print(fkl2)