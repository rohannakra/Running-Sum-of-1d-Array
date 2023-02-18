# https://leetcode.com/problems/running-sum-of-1d-array/

def running_sum(nums):
    return [sum(nums[:i+1]) for i in range(len(nums))]

print(running_sum([1, 2, 3, 4]))
print(running_sum([3, 1, 2, 10, 1]))

# ----------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]
