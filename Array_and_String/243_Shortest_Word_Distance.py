'''
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
  

Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
'''

class Solution(object):
  def shortestWordDistance(self, wordsDict, word1, word2):
    dist = len(wordsDict)
    p1, p2 = 0,0
    
    for i in range(dist):
      if wordsDict[i] == word1:
        p1 = i
      elif wordsDict[i] == word2:
        p2 = i
        
      if p1!=-1 and p2!=-1:
        dist = min(dist, abs(p1-p2)
                   
    return dist
