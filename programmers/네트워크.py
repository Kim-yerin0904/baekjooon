def dfs(i,n,computers,visited):
        visited[i] = True
        for j in range(n):
            if i != j and computers[i][j] == 1:
                if visited[j] == False:
                    dfs(j,n,computers,visited)
                
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i,n,computers,visited)
            answer += 1
    return answer
