class Solution(object):
  def validPalindrome(self, str):
    l, r = 0, len(str)-1
    while l<r:
      a = str[l].lower()
      b = str[r].lower()
      if a.isalnum() and b.isalnum():
        if a!=b:
          return False
        else:
          l+=1
          r-=1
          continue
      l, r = l+(not a.isalnum()), r-(not b.isalnum())
      
    return True
