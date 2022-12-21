'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''



class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        for i in range(len(s)):
          l = r = i
          res += self.countPali(s, l, r)
          
          l, r = i, i+1
          res += self.countPali(s, l, r)
          
        return res
          
          
    def countPali(self, s, l, r):
      res = 0
      while l >= 0 and r < len(s) and s[l]==s[r]:
        res += 1
        l-=1
        r+=1
      return res
