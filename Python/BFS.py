numOfNode = 5
start = 1
root = [[1,2], [1,3], [2,4], [2,5]]

# numOfNode: 총 노드의 개수
# start: 시작점 (맨 처음에 접근할 노드)
# root: 간선 정보들 - [노드A, 노드B]

roots = [[] for _ in range(numOfNode+1)]
# roots: 해당 노드와 연결된 모든 노드를 return하는 배열
# roots[1] 이면 노드1과 연결된 노드2,3을 return

# 간선 정보를 배열에 삽입
for info in root:
    roots[ info[0] ].append( info[1] )

visited = [False]*(numOfNode+1)
# visited: 해당 노드에 접근했는지를 나타내는 배열
# 노드1에 한 번이라도 접근했으면 visited[1] 값은 true

def bfs(start):
    queue = []
    queue.append(start)
    
    while queue:
        # 출발 노드를 가져옴
        src = queue[0]
        del queue[0]

        # 해당 노드에 접근했다고 표시
        visited[src] = True
        print(src, end=' ')
        
        # 아직 접근하지 않았다면 도착 노드를 출발 노드로 삼음
        for des in roots[src]:
            if not visited[des]:
                queue.append(des)

# 시작점부터 탐색 시작
bfs(start)