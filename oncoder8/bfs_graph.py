# undirected graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    visited = []
    queue = [start]
    print(queue)

    while queue:
        print('queue')
        print(queue)
        n = queue.pop(0) # 큐에서 뺀다.
        
        print(n)
        if n not in visited:
            visited.append(n) # 뺀걸 visited 라는 리스트에 넣어서 보여준다. 
            queue += graph[n] - set(visited) # 큐에 같은 레벨을 추가한다. 
            print('graph[n]')
            print(graph[n])
            print('set')
            print(set(visited))
    return visited

print(bfs(graph, 'A'))