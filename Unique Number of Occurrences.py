class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        b=set(arr)
        c=[]

        for i in list(b):
            c.append(arr.count(i))
        
        return len(set(c))==len(c)