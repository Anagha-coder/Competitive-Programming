# leetcode que 1
# 3 sum 
# Que: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#      Notice that the solution set must not contain duplicate triplets.

# visit: https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        # create an empty array
        result =[]
        nums.sort()
        
        length = len(nums)
        
        for i in range (length-2): # we're creating two pointers 
            # which should be ahead of i so (length -2) i.e buffer of 2 at the end 
            
            if i >0 and nums[i]==nums[i-1]: # to eliminate duplicate value
                continue
            l = i+1
            r = length-1
            
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total <0: # array : -2,-1,0,1
                    l = l+1
                elif total >0:
                    r = r-1
                    
                else: # sum = 0 
                    result.append([nums[i],nums[l],nums[r]])
                    
                    # to eliminate the duplicate no, we've done before for i only now we're doing for j & k 
                    while l<r and nums[l]==nums[l+1]:
                        l = l+1 # to skip that no
                        
                    while l<r and nums[r]==nums[r-1]:
                        r = r-1
                     
                    # if nothing happens above 2 cases we'll simply 
                    l = l+1
                    r = r-1 
                    
          
        return result
                
                    
        
