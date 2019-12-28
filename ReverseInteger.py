"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

# 32-bit. This means that the number is represented by 32 separate one’s and zero’s. 32 bits of 2 possible states = 2^32=4,294,967,296 possible values.
# Signed meaning that negative values are accepted. This halves the number of possible positive values (roughly), so the largest number you can represent is 2^31–1=2,147,483,647, but instead of 0, the smallest number you can represent is -2,147,483,648. An unsigned 32-bit integer, by contrast, can represent anything from 0 to 4,294,967,295.

class Solution:
    def reverse(self, x: int) -> int:
# if condition for negative values
# Here integer is converted to string, reversed and then converted back
        if(str(x)[0]=='-'):
            if(int(str(x)[:0:-1]) > 2**31):
                return 0
            else:
                return -1*int(str(x)[:0:-1])
# Condition for positive values
        elif int(str(x)[::-1]) > (2**31)-1:
            return 0
        else:
            return int(str(x)[::-1])
