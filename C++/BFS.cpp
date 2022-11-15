#include<iostream>
#include<vector>

using namespace std;

int numOfNode = 5;
int start = 1;
vector<vector<int>> root = {{1,2}, {1,3}, {2,4}, {2,5}};

// numOfNode: 총 노드의 개수
// start: 시작점 (맨 처음에 접근할 노드)
// root: 간선 정보들 - {노드A, 노드B}

vector<vector<int>> roots;
// roots: 해당 노드와 연결된 모든 노드를 return하는 배열
// roots[1] 이면 노드1과 연결된 노드2,3을 return

vector<bool> visited(numOfNode+1, false);
// visited: 해당 노드에 접근했는지를 나타내는 배열
// 노드1에 한 번이라도 접근했으면 visited[1] 값은 true

void bfs(int start){
    vector<int> queue;
    queue.push_back(start);

    while(queue.size() >= 1){
        // 출발 노드를 가져옴
        int src = queue[0];
        queue.erase(queue.begin());
        
        // 해당 노드에 접근했다고 표시
        visited[src] = true;
        cout << src << " ";

        // 아직 접근하지 않았다면 도착 노드를 출발 노드로 삼음
        for(int des: roots[src]){
            if(!visited[des]){
                queue.push_back(des);
            }
        }
    }
}

int main(){
    for(int i=0; i<numOfNode+1; i++){
        vector<int> empty;
        roots.push_back(empty);
    }

    // 간선 정보를 배열에 삽입
    for(int i=0; i<root.size(); i++){
        roots[root[i][0]].push_back(root[i][1]);
    }

    // 시작점부터 탐색 시작
    bfs(start);

    cout << endl;
    return 0;
}