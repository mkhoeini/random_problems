

M, N = map(int, raw_input().split())

matrix = [map(int, raw_input().split()) for i in range(M)]


def nei(i, j):
    result = []

    # Up
    if (i > 0) and (matrix[i-1][j] == 1):
        result.append((i-1, j))

    # Down
    if (i < (M-1)) and (matrix[i+1][j] == 1):
        result.append((i+1, j))

    # Left
    if (j > 0) and (matrix[i][j-1] == 1):
        result.append((i, j-1))

    # Right
    if (j < (N-1)) and (matrix[i][j+1] == 1):
        result.append((i, j+1))

    return result


graph = {
    (i, j): nei(i, j)
    for i in range(M) for j in range(N) if matrix[i][j] == 1
}


met = set()
c = 0

for node, neibors in graph.items():
    if node in met:
        continue
    else:
        c += 1
        met.add(node)
        to_meet = neibors[:]
        while len(to_meet) > 0:
            head = to_meet.pop()
            if head not in met:
                met.add(head)
                to_meet.extend(graph[head])

print "Number of islands: {}".format(c)
