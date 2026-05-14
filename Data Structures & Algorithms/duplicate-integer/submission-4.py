class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for elem in nums:
           if elem not in dic:
               dic[elem] = 1
           else:
               return True

        return False