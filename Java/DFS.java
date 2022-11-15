package pkg;

import java.util.ArrayList;
import java.util.List;

public class DFS {

	private int numOfNode = 5;
	private int start = 1;
	private int[][] root = {{1,2}, {1,3}, {2,4}, {2,5}};
	// numOfNode: 총 노드의 개수
	// start: 시작점 (맨 처음에 접근할 노드)
	// root: 간선 정보들 - {노드A, 노드B}

	private List<List<Integer>> roots = new ArrayList<>();
	// roots: 해당 노드와 연결된 모든 노드를 return하는 배열
	// roots[1] 이면 노드1과 연결된 노드2,3을 return

	private boolean[] visited = new boolean[numOfNode+1];
	// visited: 해당 노드에 접근했는지를 나타내는 배열
	// 노드1에 한 번이라도 접근했으면 visited[1] 값은 true

	public void dfs(int src){
		// 해당 노드에 접근했다고 표시
		visited[src] = true;
		System.out.print(src + " ");

		// 아직 접근하지 않았다면 도착 노드를 출발 노드로 삼음
		for(int des: roots.get(src)){
			if(!visited[des]){
				dfs(des);
			}
		}
	}
     
	public void main() {
	    for(int i=0; i<numOfNode+1; i++){
	        List<Integer> empty = new ArrayList<>();
	        roots.add(empty);
	    }
	
	    // 간선 정보를 배열에 삽입
	    for(int i=0; i<root.length; i++){
	        List<Integer> temp = roots.get(root[i][0]);
	        temp.add(root[i][1]);
	    }
	
	    // 시작점부터 탐색 시작
	    dfs(start);
	}

    public static void main(String[] args) {
        DFS main = new DFS();
        main.main();
    }
}