n = 4
numOfRoot = 5
start = 1
root = [ [1,2], [1,3], [1,4], [2,4], [3,4] ]

roots = [[] for _ in range(n+1)]

for info in root:
    roots[ info[0] ].append( info[1] )
    roots[ info[1] ].append( info[0] )

for i in range(n+1):
    roots[i].sort()

visited = [False]*(n+1)

def initialize():
    for i in range(len(visited)):
        visited[i] = False

def dfs(src):
    if not visited[src]:
        visited[src] = True
        print(src, end=' ')
        
        for des in roots[src]:
            dfs(des)

dfs(start)

initialize()
print()

def bfs(start):
    queue = []
    queue.append(start)
    
    while len(queue) >= 1:
        src = queue[0]
        del queue[0]

        if not visited[src]:
            visited[src] = True
            print(src, end=' ')
            
            for des in roots[src]:
                queue.append(des)

bfs(start)
