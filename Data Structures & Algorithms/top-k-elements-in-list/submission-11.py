class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        Map = Counter(nums).most_common()
        sol = []
        for i in range(k):
            sol.append(Map[i][0])
        
        return sol
        
                