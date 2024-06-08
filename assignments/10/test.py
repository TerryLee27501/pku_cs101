import random
from collections import deque


def generate_input_data():
    M = random.randint(1, 200)
    N = random.randint(1, 200)
    T = random.randint(0, 10)
    grid = []
    for _ in range(M):
        row = []
        for _ in range(N):
            cell_type = random.choice(['*', '*', '*', '#'])
            row.append(cell_type)
        grid.append(row)
    grid[random.randint(0, M - 1)][random.randint(0, N - 1)] = '@'  # Naruto's position
    grid[random.randint(0, M - 1)][random.randint(0, N - 1)] = '+'  # Sasuke's position
    return M, N, T, grid


M, N, T, grid = generate_input_data()
print("Generated Input:")
print(M, N, T)
for row in grid:
    print(''.join(row))


def q4(m, n, t, grid):
    graph = []
    for x in range(m):
        rs = ''.join(grid[x])  # raw string
        graph.append(rs)
        for y, l in enumerate(rs):
            if l == '@':
                s = [x, y]
            if l == '+':
                d = [x, y]

    v = [s]
    q = deque([[s, 0, t]])
    while q:
        cp, time, hits = q.popleft()
        v.append(cp)
        if cp == d:
            return time

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ori_nps = [[cp[0] + ix, cp[1] + iy] for ix, iy in dirs]
        nps = []
        for npx, npy in ori_nps:
            if npx >= m or npx < 0 or npy >= n or npy < 0 or [npx, npy] in v:
                continue
            nps.append([npx, npy])
        v.extend(nps)
        for np in nps:
            if graph[np[0]][np[1]] == '#':
                if hits > 0:
                    q.append([np, time + 1, hits - 1])
            else:
                q.append([np, time + 1, hits])

    return -1


def min_time_to_catch_sasuke(M, N, T, grid):
    graph = []
    for row in grid:
        graph.append(''.join(row))
    direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    start, end = None, None
    for i in range(M):
        for j in range(N):
            if graph[i][j] == '@':
                start = (i, j)

    def bfs():
        q = deque([start + (T, 0)])
        visited = [[-1] * N for i in range(M)]
        visited[start[0]][start[1]] = T
        while q:
            x, y, t, time = q.popleft()
            time += 1
            for dx, dy in direc:
                if 0 <= x + dx < M and 0 <= y + dy < N:
                    if (elem := graph[x + dx][y + dy]) == '*' and t > visited[x + dx][y + dy]:
                        visited[x + dx][y + dy] = t
                        q.append((x + dx, y + dy, t, time))
                    elif elem == '#' and t > 0 and t - 1 > visited[x + dx][y + dy]:
                        visited[x + dx][y + dy] = t - 1
                        q.append((x + dx, y + dy, t - 1, time))
                    elif elem == '+':
                        return time
        return -1
    return bfs()


print("Your Code Result:", q4(M, N, T, grid))
print("My Code Result:", min_time_to_catch_sasuke(M, N, T, grid))
