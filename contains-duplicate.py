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
      
      
      
Sorting --> Time O(n log n) / Memory O(1)
 class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums) 
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                    return True
        return False
      
  /*alternate* try using nums.sort() insead of sorted(nums) /
  
