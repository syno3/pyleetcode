class Easyfunctions:
    
    def twosum(self, nums, target:int):
        """ 
        challenge
        _________
        
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
        
        solution
        ________
        
        create a dictionary, get the difference between elements and target, check if number exist in hashmap, add compliment incase it dosent
        
        """
        hashMap = dict()
        
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            
            if num in hashMap:
                return [hashMap[num], i]
            else:
                hashMap[complement] = i
                
    def palindrome(self):
        pass
