

def DFSUtil(G, v, visited, deep, paths):
    visited.add(v)
    neighbours = sorted(G[v])
    
    for neighbour in neighbours:
        if neighbour not in visited:
            path = f'{v}-{neighbour} pathR(G,{neighbour})'
            print(path.rjust((deep*2)+len(path)+2))
            DFSUtil(G, neighbour, visited, deep+1, paths)
            paths[v][neighbour] = True
        elif not paths[v][neighbour]:
            path = f'{v}-{neighbour}'
            print(path.rjust((deep*2)+len(path)+2))


def DFS(G):
    visited = set()
    paths = [[False for _ in range(20)] for _ in range(20)]
    
    for v in range(len(G)):
        if v not in visited:
            DFSUtil(G, v, visited, 0, paths)
            if len(G[v]) > 0:
                print()


def case(i):
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]

    for _ in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
    
    print('{:>2}'.format(f"Caso {i}:"))
    DFS(G)


N = int(input())

for i in range(1, N+1):
    case(i)
