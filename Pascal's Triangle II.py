class Solution:
    """
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    """
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        prev=1

        for i in range(1, rowIndex+1):
            next= prev*(rowIndex-i+1)//i
            row.append(next)
            prev=next
        
        return row 