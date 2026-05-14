class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            base = 1
            for k in range(len(nums)):
                if k != i:
                    base *= nums[k]
            res.append(base)
        return res
            