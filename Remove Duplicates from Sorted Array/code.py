class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            y=nums[0]
            length = len(nums)
            x=1
            while x<length:
                if y==nums[x]:
                    nums.pop(x)
                    length-=1
                else:
                    y=nums[x]
                    x+=1
            return length
        else:
            return 0