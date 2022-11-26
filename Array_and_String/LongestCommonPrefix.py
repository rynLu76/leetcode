class Solution(object):
  def LongestCommonPrefix(self, strs):
    m, M, i, = min(strs), max(strs), 0
    
    for i in range(min(len(m), len(M))):
      if m[i] != M[i]:
        break
       else:
        i+=1
        
    return m[:i]
