// Programmers - Stack And Queue - 프린터

import java.util.LinkedList;
import java.util.PriorityQueue;

class Solution {
	LinkedList<Integer> ll = new LinkedList<Integer>();
	PriorityQueue<Integer> lstPrior = new PriorityQueue<Integer>();

	int Max(int n1, int n2) {
		return n1 > n2 ? n1 : n2;
	}

	public int solution(int[] priorities, int location) {
		int answer = 0;

		for (int i = 0; i < priorities.length; i++) {
			lstPrior.add(-priorities[i]);
			ll.add(i);
		}

		int temp;
		while(-lstPrior.peek()!=priorities[ll.getFirst()] || ll.getFirst()!=location) {
			if(-lstPrior.peek()==priorities[ll.getFirst()]) {
				answer+=1;
				ll.pollFirst();
				lstPrior.poll();
			}
			else {
				temp=ll.pollFirst();
				ll.add(temp);
			}
		}

		return answer+1;
	}
}
