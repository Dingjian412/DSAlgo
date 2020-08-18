graph={
    "A":["C","B"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}


def bfs(graph,s):
    queue=[]
    queue.append(s)
    seen=set() #set, it contains vertex that we have seen
    seen.add(s)
    while(queue):
        vertex=queue.pop(0)
        nodes=graph[vertex]
        for w in nodes:
            if w not in seen:
                seen.add(w)
                queue.append(w)
        print(vertex)

# e: end vertext. s: start vertetx
def bfsPath(graph, s, e):
    queue = []
    queue.append(s)
    seen = set()  # set, it contains vertex that we have seen
    seen.add(s)
    parent={s:None}
    while (queue):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                seen.add(w)
                queue.append(w)
                parent[w]=vertex
        # print(vertex)
    print(parent)
    v=e
    count =-1
    while v != None:
        count+=1
        print(v)
        v=parent[v]
    return count

