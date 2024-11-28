# Heapsort
import heapq
nums = [1, 2, 3, 4, 5]
heapq.heapify(nums) # 0(n)
while nums:
    heapq.heappop(nums) # 0(logn)

# Mergesort
# (and most built-in sort functions)