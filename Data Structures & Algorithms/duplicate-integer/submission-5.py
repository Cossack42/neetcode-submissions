class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for i in range(0,len(nums)):
            dict1[nums[i]]=0
        for i in range(0,len(nums)):
            dict1[nums[i]]+=1
        for i in range(0,len(nums)):
            if dict1[nums[i]]>=2:
                return True
        return False