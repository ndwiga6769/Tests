# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash table to store elements and their indices
        hash_table = {}
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            # Check if the complement exists in the hash table
            if complement in hash_table:
                # If it exists, return the indices
                return [hash_table[complement], i]
            # If it doesn't exist, add the current element to the hash table
            hash_table[num] = i
        # If no solution is found, return an empty list
        return []
   
# Example usage: 
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1]
  