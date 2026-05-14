class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for idx, elem in enumerate(nums):
            diff = target - elem
            if diff not in Map:
                Map[elem] = idx
            
            else:
                return [Map.get(diff), idx]
                