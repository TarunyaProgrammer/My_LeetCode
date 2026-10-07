# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m_cord = []
#         n = len(matrix)
#         m = len(matrix[0])
#         for i in range(n):
#             if 0 in matrix[i]:
#                 for j in range(m):
#                     if matrix[i][j]==0:m_cord.append(j)
#                 matrix[i] = [0]*m
#         for i in range(n):
#             for j in range(m):
#                 if j in m_cord:
#                     matrix[i][j] = 0



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        r_track = [0]*n
        c_track = [0]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    r_track[i] = -1
                    c_track[j] = -1

        for i in range(n):
            for j in range(m):
                if r_track[i] == -1 or c_track[j] == -1:
                    matrix[i][j] = 0





# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         cord = []
#         n = len(matrix)
#         m = len(matrix[0])
#         print(n)
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0 :
#                     cord.append(i)
#                     cord.append(j)

#         for i in range(0,len(cord),2):
#             matrix[cord[i]] = [0] * m

#         for j in range(1,len(cord),2):
#             for i in range(n):
#                 matrix[i][cord[j]] = 0