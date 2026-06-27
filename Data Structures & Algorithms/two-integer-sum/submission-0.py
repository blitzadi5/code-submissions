class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mm={}
        for i,j in enumerate(nums):
            d=target-j
            if d in mm:
                return [mm[d],i]
            mm[j]=i
        return

            
