// Programmers - Stack And Queue - 기능개발

import java.util.LinkedList;

class Solution {
    LinkedList<Integer> ll = new LinkedList<Integer>();
    LinkedList<Integer> spd = new LinkedList<Integer>();
    LinkedList<Integer> ans = new LinkedList<Integer>();
    
    int updateLL(){
        int ret=0;
        while(!ll.isEmpty() && ll.getFirst()>=100){
            ll.pollFirst(); spd.pollFirst();
            ret+=1;
        }
        return ret;
    }
    
    public int[] solution(int[] progresses, int[] speeds) {
        for(int i=0;i<progresses.length;i++){
            ll.add(progresses[i]); spd.add(speeds[i]);
        } // setting
        
        int sz; int temp;
        while(!ll.isEmpty()){
            sz=ll.size();
            for(int i=0;i<sz;i++){
                if(ll.get(i)<100) {
                    temp=ll.get(i)+spd.get(i);
                    ll.set(i,temp);
                }
            }
            if(ll.getFirst()>=100) ans.add(updateLL());
        }
        
        int[] answer = new int[ans.size()];
        
        int k=0;
        while(!ans.isEmpty()){
            answer[k++]=ans.pollFirst();
        }
        
        return answer;
    }
}
