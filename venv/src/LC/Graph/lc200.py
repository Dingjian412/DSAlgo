# [LeetCode] 200. Number of Islands_ Medium tag: BFS
# 这个题目也是经典的BFS, 思路就是将2D array扫一遍, 然后每次如果扫到的元素是'1' and not in visited, ans += 1,
# 并且建一个queue, 将所有跟它相邻的4个元素如果是'1' 并且没有visited过的,
# append进入queue, mark 为visited, recursively直到把所有4个方向的'1' 的元素都mark为visited, 然后一直把整个array扫完, 然后return ans.
def numIslands(grid):
    ans=0
    if not grid or len(grid[0]) == 0: return ans
    queue=[]
    visited=set()
    lr=len(grid)
    lc=len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(lr):
        for j in range(lc):
            if grid[i][j]=='1' and (i,j) not in visited:
                ans+=1
                visited.add((i,j))
                queue.append((i,j))
                while(queue):
                    r,c=queue.pop(0)
                    for d1,d2 in dirs:
                        nr,nc=r+d1,c+d2
                        if 0<=nr<lr and 0<=nc<lc and grid[nr][nc]=='1' and (nr,nc) not in visited:
                            queue.append((nr,nc))
                            visited.add((nr,nc))
    return ans


grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(f"{len(grid)} rows,{len(grid[0])} columns")
print(numIslands(grid))


