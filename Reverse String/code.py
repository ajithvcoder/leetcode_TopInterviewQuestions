"""

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

you must do this by modifying the input array in-place with O(1) extra memory.


"""




class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #print(reversed(s))
        # result=[]
        # for i in reversed(s):
        #     result.append(i)
        # s=result
        # #s=s[::-1]
        s.reverse()
        