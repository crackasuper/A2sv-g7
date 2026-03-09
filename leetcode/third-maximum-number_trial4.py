class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) < 3:
        #     return max(nums)
        
        # else:


        #     for value in nums:
        #         while nums.count(value) > 1:
        #             nums.remove(value)
            
        #     nums = sorted(nums)

        #     return nums[-3]

        # nums = set(nums)
        # ans = list(nums)

        # if len(ans) >= 3:
        #     return ans[-3]

        # else:
        #     return max(ans)

        # first_maximum = second_maximum =third_maximum = float('inf')
        # for num in nums:

        #     for num in [first_maximum, second_maximum, third_maximum]:
        #         continue


        #     if num > first_maximum:
        #         third_maximum, second_maximum, first_maximum = second_maximum, first_maximum, num
        #     elif num > second_maximum:
        #         third_maximum, second_maximum = second_maximum, num
            
        #     elif num > third_maximum:
        #         third_maximum = num
           

 
        # if third_maximum != float('inf'):
        #     return third_maximum
        # else:
        #     return first_maximum

        first_max = second_max = third_max = float('-inf')
      
    
        for num in nums:
         
            if num in [first_max, second_max, third_max]:
                continue
          
  
            if num > first_max:
      
                third_max, second_max, first_max = second_max, first_max, num
            elif num > second_max:
         
                third_max, second_max = second_max, num
            elif num > third_max:
      
                third_max = num
      
        return third_max if third_max != float('-inf') else first_max