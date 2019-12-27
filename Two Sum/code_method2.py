class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:len(nums)]:
                return [i,i+1+nums[i+1:len(nums)].index(target-nums[i])]
                break
