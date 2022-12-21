'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''



class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        Option 1: If rob, then rob = not_rob + nums[i]
        (max money if rob the current house = max money if not rob the last house + amount of the current house)
        Option 2: If not rob, then not_rob = max(rob, not_rob)
        (max money if not rob the current house = max money at the last house, either rob or not rob)

        Varibles: rob = max money if rob the current house
        not_rob = max money if not rob the current house.
        Both variables are initially set to 0

        Complexity:
        time = O(n)
        Space = O(1)
        '''
        rob, not_rob = 0,0
        for num in nums:
          rob = not_rab + num
          not_rob = max(rab, not_rab)
        return max(rab, not_rab)
