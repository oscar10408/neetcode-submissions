class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sets = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in sets:
                length = 1
                while (i+length in sets):
                    length += 1
                longest = max(longest, length)
        
        return longest
                