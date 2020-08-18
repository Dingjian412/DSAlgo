#below code has error, try to understand tree.
def distanceK(root,target,k):
    def dfs(node, par = None):
        if node:
            node.par = par
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)

    queue = collections.deque([(target, 0)])
    seen = {target}
    while queue:
        if queue[0][1] == k:
            return [node.val for node, d in queue]
        node, d = queue.popleft()
        for nei in (node.left, node.right, node.par):
            if nei and nei not in seen:
                seen.add(nei)
                queue.append((nei, d+1))

    return []

root = [3,5,1,6,2,0,8,None,None,7,4]
target=5
k=2
result=distanceK(root,target,k)
print(result)

