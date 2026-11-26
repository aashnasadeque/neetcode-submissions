class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curSum = 0
        prefixSums = { 0 : 1 }

        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k
            result += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return result