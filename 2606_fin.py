def dfs(graph, start_node,com_num):
    need_visited = list()
    visited = list(0 for _ in range(com_num))
    
    need_visited.append(start_node-1)

    while need_visited:
        node = need_visited.pop()
        
        visited[node]=1
        
        for i in range(com_num):
            if graph[node][i] == 1 and visited[i]==0:
                need_visited.append(i)
    count=0     
    for j in range(com_num):
        if visited[j] == 1:
            count+=1
    return count-1

com_num = int(input())
couple = int(input())

graph=[]

for _ in range(com_num):
    graph.append(list(0 for _ in range(com_num)))

for i in range(couple):
    com_a,com_b = map(int,input().split())
    graph[com_a-1][com_b-1] = 1
    graph[com_b-1][com_a-1] = 1

print(dfs(graph,1,com_num))

