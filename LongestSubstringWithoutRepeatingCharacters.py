"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


s = "pwwkew"
l=[]
l[:0]=s
j=0
ans=1
while j != len(s)-1:
    for i in range(len(s)):
        if len(l[j:i+1])>ans and (l[j:i+1]!=[]) and len(l[j:i+1])== len(set(l[j:i+1])):
            ans=len(l[j:i+1])
            print(l[j:i+1])
    j=j+1
print(ans)
