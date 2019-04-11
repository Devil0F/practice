#某公司面试题
M,N = list(map(int,raw_input().split(',')))
book = [[1,1,1,0,1],[1,1,1,0,1],[1,1,1,0,1],[0,0,0,0,1],[1,1,1,0,1]]

#for i in range(M):
	#line = list(map(int,raw_input().split(',')))
	#book.append(line)
print(book)	
class Solution:
	def __init__(self,grid):
		self.grid = grid
		self.cnt = 0
		self.dp = []
		
	def dfs(self,i,j):
		if 0 <= i <M and 0 <= j < N:
			if self.grid[i][j] == 1:
				self.cnt += 1
				self.grid[i][j] = 0
				self.dfs(i-1,j)
				self.dfs(i+1,j)
				self.dfs(i,j-1)
				self.dfs(i,j+1)
				self.dfs(i-1,j-1)
				self.dfs(i-1,j+1)
				self.dfs(i+1,j-1)
				self.dfs(i+1,j+1)
	def solve(self):
		for i in range(M):
			for j in range(N):
				if self.grid[i][j] == 1:
					self.cnt = 0
					self.dfs(i,j)
					if self.cnt > 0:
						self.dp.append(self.cnt)
					
		return len(self.dp),max(self.dp),min(self.dp)
		
a = Solution(book)
b,c,d = a.solve()
print(b,c,d)
