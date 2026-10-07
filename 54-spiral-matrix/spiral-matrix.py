class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:

        top,bot,left,right = 0,len(mat)-1,0,len(mat[0])-1

        res = []

        while top<=bot and left<=right:
            for i in range(left,right+1):res.append(mat[top][i])
            top+=1
            for i in range(top,bot+1):res.append(mat[i][right])
            right-=1
            if top<=bot:
                for i in range(right,left-1,-1):res.append(mat[bot][i])
                bot-=1
            if left<=right:
                for i in range(bot,top-1,-1):res.append(mat[i][left])
                left+=1

        return res