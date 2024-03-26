import heapq
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Step 1: Combine corresponding elements of nums1 and nums2 into pairs.
        pairs = [(num1, num2) for num1, num2 in zip(nums1, nums2)]
        
        # Step 2: Sort the pairs based on the second element (nums2) in descending order.
        sorted_pairs = sorted(pairs, key=lambda pair: pair[1], reverse=True)
        
        # Step 3: Initialize a min heap to keep track of the minimum elements from nums1.
        min_heap = []
        
        # Step 4: Initialize variables to track the sum of nums1 and the minimum element from nums2.
        sum_nums1, min_nums2 = 0, float("inf")
        
        # Step 5: Initialize a variable to store the maximum score.
        max_score = 0
        
        # Step 6: Iterate through each pair in sorted_pairs.
        for num1, num2 in sorted_pairs:
            # Step 7: Add the current nums1 element to the sum.
            sum_nums1 += num1
            
            # Step 8: Push the current nums1 element to the min_heap.
            heapq.heappush(min_heap, num1)
            
            # Step 9: If the size of min_heap exceeds k, pop the minimum element.
            if len(min_heap) > k:
                popped_num1 = heapq.heappop(min_heap)
                sum_nums1 -= popped_num1
            
            # Step 10: If the size of min_heap equals k, calculate the score and update max_score if necessary.
            if len(min_heap) == k:
                score = sum_nums1 * num2
                max_score = max(max_score, score)
        
        # Step 11: Return the maximum score.
        return max_score
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    nums1_1 = [1,3,3,2]
    nums1_2 = [2,1,3,4]
    k1_1 = 3
    ms1 = sol.maxScore(nums1_1, nums1_2, k1_1)
    print(ms1)
    # Example 2
    nums2_1 = [4,2,3,1,1]
    nums2_2 = [7,5,10,9,6]
    k2_1 = 1
    ms2 = sol.maxScore(nums2_1, nums2_2, k2_1)
    print(ms2)