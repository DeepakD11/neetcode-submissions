class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.sum = 0
        self.SumMatrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(self.SumMatrix)):
            for j in range(len(self.SumMatrix[0])):
                self.SumMatrix[i][j] = matrix[i][j]
                if i==0 and j!= 0:
                    self.SumMatrix[i][j] = self.SumMatrix[i][j] + self.SumMatrix[i][j-1]
                if j==0 and i!=0:
                    self.SumMatrix[i][j] = self.SumMatrix[i][j] + self.SumMatrix[i-1][j]
                if i!=0 and j!=0:
                    self.SumMatrix[i][j] = self.SumMatrix[i][j] + self.SumMatrix[i-1][j] + self.SumMatrix[i][j-1] - self.SumMatrix[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:        
        total = self.SumMatrix[row2][col2]

        if row1 > 0:
            total -= self.SumMatrix[row1-1][col2]

        if col1 > 0:
            total -= self.SumMatrix[row2][col1-1]

        if row1 > 0 and col1 > 0:
            total += self.SumMatrix[row1-1][col1-1]

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)