// programmers - Graph - 가장 먼 노드
import java.util.LinkedList;
import java.util.Queue;

class Solution3 {
	int[] dst;
	boolean[][] grph;
	int mx;
	
	void bfs(int n) {
		Queue<Integer> que = new LinkedList<Integer>();
		que.add(1);

		while (!que.isEmpty()) {
			int i = que.poll();

			for (int j = 2; j <= n; j++) {
				if (dst[j] == 0 && grph[i][j]) {
					dst[j] = dst[i] + 1;
					que.add(j);
					mx = Math.max(mx, dst[j]);
				}
			}
		}
	}

	public int solution(int n, int[][] edge) {
		int answer=0;
		
		dst = new int[n + 1];
		grph = new boolean[n + 1][n + 1];

		for (int i = 0; i < edge.length; i++)
			grph[edge[i][0]][edge[i][1]] = grph[edge[i][1]][edge[i][0]] = true;
		

		for (int d : dst) {
			if (mx == d)
				answer+=1;
		}

		return answer;

	}
}
