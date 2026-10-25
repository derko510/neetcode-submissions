class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} # hash map

        # loop thru nums 
        for n in nums:
            # build hash map from nums 
            count[n] = count.get(n, 0) + 1

        # build buckets for each count
        buckets = [[] for _ in range(len(nums) + 1)]
        # counting nums that get added to bucket 
        for num, c in count.items():
            buckets[c].append(num)

        res = []
        # loop through bucket indexes from highest to lowest
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res