https://leetcode.com/problems/contains-duplicate/

code 1 brute force 
Time complexity  : o(n2)
Space complexity : o(1): 
  
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
