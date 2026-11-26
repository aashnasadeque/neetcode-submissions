class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        store = sorted(set(nums))
        best = 1
        curr = 1
        

        for i in range(1, len(store)):
            if store[i] == store[i - 1] + 1:
                curr += 1
            else:
                curr = 1
            best = max(best, curr)
        return best