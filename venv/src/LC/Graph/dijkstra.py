import heapq
import math

def init_distance(graph,s):
    distance={s:0}
    for vertex in graph:
        if vertex!=s:
            distance[vertex]=math.inf
    return distance

# e: end vertext. s: start vertetx
def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue,(0,s))
    visited = set()  # set, it contains vertex that we have visited
    parent={s:None}
    distance=init_distance(graph,s)
    # print(f'This is pqueue:{pqueue},type is {type(pqueue)}')
    # print(f"set type is {type(visited)}")
    # print(f"parent type is {type(parent)}")
    # print(f'This is distance:{distance},type is {type(distance)}')
    while (pqueue):
        # print(f'pqueue has these elements:{pqueue}')
        # (0,'A')
        pair = heapq.heappop(pqueue)
        # print(f'pop an element is:{pair}')
        dist=pair[0]
        vertex=pair[1]
        visited.add(vertex)
        # print(f'we have visited these vertexs:{visited}')
        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in visited:
                distToStart=dist+graph[vertex][w]
                if distToStart<distance[w]:
                    heapq.heappush(pqueue,(distToStart,w))
                    parent[w]=vertex
                    distance[w]=distToStart
    return parent,distance

graph={
    "A":{"B":5,"C":1},
    "B":{"A":5,"C":2,"D":1},
    "C":{"A":1,"B":2,"D":4,"E":8},
    "D":{"B":1,"C":4,"E":3,"F":6},
    "E":{"C":8,"D":3},
    "F":{"D":6}
}
parent,distance=dijkstra(graph,'A')
print(parent)
print(distance)