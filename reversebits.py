class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for _ in range(32):
            result= result << 1
            bit=n%2
            result+=bit
            n=n>>1
        
        return result