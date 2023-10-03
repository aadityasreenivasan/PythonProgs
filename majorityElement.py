class Solution:
    def majorityElement(nums):
        """
        return majority element from a list
        param: nums-list of integers
        """
        res= None
        c=0

        for i in nums:
            if c==0:
                res=i
            c+=(1 if i==res else -1)
        
        return res