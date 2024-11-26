def solution(begin, target, words):
    words.insert(0,begin)
    if target not in words:
        return 0
    else:
        visited = [0] * (len(words))
        depth = [1] * (len(words))
        queue = [begin]
        visited[0] += 1
        target_index = words.index(target)
        while queue:
            begin = queue.pop(0)
            for i in range(len(words)):
                wrong = 0
                for j in range(len(begin)):
                    if begin[j] != words[i][j]:
                        wrong += 1
                if wrong ==1 and visited[i] == 0:
                    queue.append(words[i])
                    if depth[i] == 1:
                        depth[i] = depth[words.index(begin)]+1
                visited[words.index(begin)] = 1
            if depth[target_index] != 1:
                return depth[target_index]-1
            
