// Programmers - Heap - 라면공장

import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public int solution(int stock, int[] dates, int[] supplies, int k) {
        PriorityQueue<Integer> que = new PriorityQueue<>(Comparator.reverseOrder());
        int answer=0;
        int index=0;
        for(int i=0;i<k;i++){
            if(index<dates.length && i==dates[index]){
                que.add(supplies[index++]);
            }
            if(stock==0) {
                stock+=que.poll();
                answer++;
            }
            stock--;
        }
        
        return answer;
    }
}
