// Programmers - Brute Force - 모의고사

import java.util.Arrays;
import java.util.LinkedList;

class Solution {

	int Max(int n1, int n2) {
		return n1 > n2 ? n1 : n2;
	}

	public int[] solution(int[] answers) {
		LinkedList<Integer> ll = new LinkedList<>();

		int[][] supo= {{1, 2, 3, 4, 5},{2, 1, 2, 3, 2, 4, 2, 5},{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
		
		int[] sp = new int[3];
		int[] answer;

		for (int i = 0; i < answers.length; i++) {
			for (int j = 0; j < 3; j++) {
				if (supo[j][i % supo[j].length] == answers[i])
					sp[j] += 1;
			}
		}

		int mx = 0;
		for (int i = 0; i < 3; i++) {
			mx = Max(mx, sp[i]);
		}
		for (int i = 0; i < 3; i++)
			if (sp[i] == mx)
				ll.add(i + 1);

		answer = new int[ll.size()];
		int k = 0;
		while (!ll.isEmpty())
			answer[k++] = ll.pollFirst();

		return answer;
	}
}
