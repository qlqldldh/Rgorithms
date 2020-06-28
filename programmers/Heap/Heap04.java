// Programmers - Heap - 이중우선순위큐 

import java.util.PriorityQueue;
import java.util.Comparator;

public class Solution {
	public int[] solution(String[] operations) {
		int[] answer = new int[2];
		PriorityQueue<Integer> maxTop = new PriorityQueue<>(Comparator.reverseOrder());
		PriorityQueue<Integer> minTop = new PriorityQueue<>();
		
		String[] strs; int temp;
		for(int i=0;i<operations.length;i++) {
			strs=operations[i].split(" ");
			if(strs[0].equals("I")) {
				maxTop.add(Integer.parseInt(strs[1]));
				minTop.add(Integer.parseInt(strs[1]));
			} else {
				if (!minTop.isEmpty()) {
					if (strs[1].equals("1")) {
						temp = maxTop.poll();
						minTop.remove(temp);
					} else {
						temp=minTop.poll();
						maxTop.remove(temp);
					}
				}
			}
		}
		if(minTop.isEmpty()) {
			answer[0]=0;
			answer[1]=0;
		} else {
			answer[0]=maxTop.poll();
			answer[1]=minTop.poll();
		}
		
		return answer;
	}
}
