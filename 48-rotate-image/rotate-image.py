class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix)
        # res = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         res[j][n-i-1] = matrix[i][j]

        # for i in range(n):
        #     for j in range(n):
        #         # Store rotated value in original matrix
        #         matrix[i][j] = res[i][j]




        n = len(mat)
        for i in range(0, n-1):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i],mat[i][j]
        for i in range(n):
            mat[i].reverse()