# [LeetCode] 695. Max Area of Island_Medium tag: DFS/BFS
def maxAreaOfIsland(grid):
    ans=0
    if not grid or len(grid[0])==0: return ans
    queue=[]
    visited=set()
    lr=len(grid)
    lc=len(grid[0])
    dirs=[(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(lr):
        for j in range(lc):
            if grid[i][j]==1 and (i,j) not in visited:
                queue.append((i,j))
                visited.add((i,j))
                count=1
                while(queue):
                    ni,nj=queue.pop(0)
                    for r,c in dirs:
                        nr,nc=ni+r,nj+c
                        if 0<=nr<lr and 0<=nc<lc and grid[nr][nc]==1 and (nr,nc) not in visited:
                            queue.append((nr,nc))
                            count+=1
                            visited.add((nr,nc))
                if count>ans: ans=count
    return ans


grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,1,1,0,1,0,0,0,0,0,0,0,0],
      [0,1,0,0,1,1,0,0,1,0,1,0,0],
      [0,1,0,0,1,1,0,0,1,1,1,0,0],
      [0,0,0,0,0,0,0,0,0,0,1,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# grid=[[1,1,0,0,0],
#       [1,1,0,0,0],
#       [0,0,0,1,1],
#       [0,0,0,1,1]]
print(maxAreaOfIsland(grid))