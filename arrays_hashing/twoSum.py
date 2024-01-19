from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for key, value in enumerate(nums):
            difference = target - value
            if difference in hashmap:
                return [hashmap[difference], key]
            hashmap[value] = key
            
