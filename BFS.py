import collections
visited_node = set()
return_list=[]

def bfs(visited_node,graph,node):
    visited_node.add(node)
    queue = collections.deque([node])
    # queue.append(node)

    while queue:   # queue is not empty
        m = queue.popleft()
        # print(m)
        return_list.append(m)
        for edges in graph[m]:
            if edges not in visited_node:
                visited_node.add(edges)
                queue.append(edges)
    return return_list


visit_node = set()
stack=[]
result = []
def dfs(visit_node,graph,node):
    stack.append(node)
    while len(stack)>0:
        node = stack.pop()
        result.append(node)
        if node not in visit_node:
            visit_node.add(node)
            for neighbour in graph[node]:
                stack.append(neighbour)

    return result

graph = { 5:[3,7], 3:[2,4],
       7:[8], 2:[],
       4:[], 8:[9], 9:[] }

print("BFS")
obj = bfs(visited_node,graph,5)
print(obj)

print("DFS")
obj1 = dfs(visit_node,graph,5)
print(obj1)