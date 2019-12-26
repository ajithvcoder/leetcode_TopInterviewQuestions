Two Sum problem : Easy 

    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            
            result=[]
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target:
                        result.append(i)
                        result.append(j)                   
                        
            
            return result

A function twoSum() is created under a class . it says that 

    def twoSum(self, nums: List[int], target: int) -> List[int]:

nums is a List with int input and then target is a input with int input 
and then it returns a list which is of int type

    result=[]

A empty list return is created 

    for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target:

We are comparing pair of numbers starting from left to right by their index.if 
both numbers add to target then we are appending corresponding 
index.





