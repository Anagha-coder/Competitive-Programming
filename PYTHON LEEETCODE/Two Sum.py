# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# ex:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# visit :  https://leetcode.com/problems/two-sum/



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        foundsol = False
        i=0
        
        sollist=[]
        while i < len(nums) and not foundsol:
            j = i + 1
            while j < len(nums) and not foundsol:
                if nums[i] + nums[j] == target:
                    foundsol = True 
                    sollist.append(i)
                    sollist.append(j)
                j+=1    
        i+=1
            
        return sollist    
    
    
 # or sol2

class Solution(object):
    def twoSum(self, nums, target):
        dictx = {}
        len_of_nums = len(nums)
        i = 0
        while i < len_of_nums:
            j = target - nums[i]
            if j in dictx:
                return(dictx[j],i)
            dictx[nums[i]]=i
            i+=1
