# [LeetCode] 733. Flood Fill_Easy tag: BFS
def floodFill(image,sr,sc,newColor):
    lr=len(image)
    lc=len(image[0])
    oricolor=image[sr][sc]
    ans=image

    if oricolor == newColor: return ans

    queue=[]
    queue.append((sr,sc))
    visited=set()
    dirs=[(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        pr, pc = queue.pop(0)
        ans[pr][pc] = newColor
        visited.add((pr, pc))
        for d1, d2 in dirs:
            nr, nc = pr + d1, pc + d2
            if 0 <= nr < lr and 0 <= nc < lc and image[nr][nc] == oricolor and (nr, nc) not in visited:
                queue.append((nr, nc))
    return ans


image=[[1,1,1],
       [1,1,0],
       [1,0,1],
       [1,0,1]]
sr=1
sc=1
newColor=2
print(floodFill(image,sr,sc,newColor))
