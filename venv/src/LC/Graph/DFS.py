graph={
    "A":["C","B"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}

def dfs(graph,s):
    stack=[]
    stack.append(s)
    seen=set() #set, it contains vertex that we have seen
    seen.add(s)
    while(stack):
        vertex=stack.pop()
        nodes=graph[vertex]
        for w in nodes:
            if w not in seen:
                seen.add(w)
                stack.append(w)
        print(vertex)



