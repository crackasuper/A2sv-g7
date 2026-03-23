class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        temp = sum(nums[:k])
        ans = temp
        for i in range(k, len(nums)):
            temp += nums[i] - nums[i - k]
            ans = max(ans, temp)
        return ans / k
