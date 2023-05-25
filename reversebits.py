class Solution:
    def reverseBits(self, n: int) -> int:
        """
        returns bits in reverse
        param: n- integer tobe reversed in bit format
        """
        result=0
        for _ in range(32):
            result= result << 1
            bit=n%2
            result+=bit
            n=n>>1
        
        return result