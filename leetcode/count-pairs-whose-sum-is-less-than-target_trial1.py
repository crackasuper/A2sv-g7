class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        counts = 0
        # for idx in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if nums[idx] + nums[j] < target:
        #             counts += 1

        for i , j in enumerate(nums):
            left_bound = bisect_left(nums, target - j, hi=i)

            counts += left_bound


        return counts