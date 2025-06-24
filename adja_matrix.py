import collections
from collections import deque
def bfs(mat, i, visited):
    """
   A(0) [[1, 1, 0],
   B(1) [1, 1, 0],
   C(2) [0, 0, 1]]
    :return:
    """
    n = len(mat)
    q = collections.deque([i])

    while q:
        cur_node = q.popleft()
        visited[cur_node] = True
        for i in range(n):
            if mat[cur_node][i]==1 and visited[i]==False:
                q.append(i)

def solution(mat):
    num_prov = 0
    visited = [False] * len(mat)
    for i in range(len(mat)):
        if not visited[i]:
            num_prov += 1
            bfs(mat, i, visited)
    return num_prov

if __name__ == "__main__":
    mat = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(mat))

    # num_nodes = len(am)
    # visited = [False] * num_nodes
    # r = []
    # dq = deque([2])
    # while dq:
    #     current_node = dq.popleft()
    #     r.append(current_node)
    #     visited[current_node] = True
    #     for i in range(num_nodes):
    #         if am[current_node][i] == 1 and not visited[i]:
    #             dq.append(i)
    # return r