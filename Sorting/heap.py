import heapq
a = [3, 5, 1, 2, 6, 8, 7]

heapq.heapify(a)
k=sum(a)
print(k+1)

heapq.heappush(a, -10)

print(a)