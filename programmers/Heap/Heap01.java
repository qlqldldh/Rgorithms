// Programmers - Heap - 더 맵게

import java.util.PriorityQueue;

class Solution {
    PriorityQueue<Integer> foods = new PriorityQueue<>();
	
	public int solution(int[] scoville, int K) {
		int answer=0;
		
		for(int i=0;i<scoville.length;i++) foods.add(scoville[i]);
		
		int temp;
		while (foods.peek() < K) {
			if(foods.size()<=1) {
				return -1;
			}
			temp = foods.poll();
			temp += foods.poll() * 2;
			foods.add(temp);
			answer += 1;
		}
		
		return answer;
	}
}
