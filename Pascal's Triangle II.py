class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        prev=1

        for i in range(1, rowIndex+1):
            next= prev*(rowIndex-i+1)//i
            row.append(next)
            prev=next
        
        return row 