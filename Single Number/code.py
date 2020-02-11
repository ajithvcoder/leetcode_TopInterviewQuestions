class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictOne={}
        for i in nums:
            if i in dictOne.keys():
                dictOne[i]+=1
            else:
                dictOne[i]=1
        print(dictOne)
        for key,val in dictOne.items():
            if val==1:
                return key