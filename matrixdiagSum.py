class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        returns sum of of diagonals in a matrix:
        [x][][x]
        [][x][]
        [x][][x]
        param: mat- 2D matrix
        """
        l=len(mat)
        if l==1: return mat[0][0]

        sum=0
        #iterating through array Diagonals
        for i in range(l):
            sum+=mat[i][i]
            sum+=mat[i][-1-i]
        
        if l%2==1:
            sum-=mat[l//2][l//2]
        
        return sum