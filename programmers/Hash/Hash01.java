
// Programmers - Hash - 완주하지 못한 선수

import java.util.HashSet;
import java.util.Iterator;
import java.util.HashMap;

class Solution {
    HashSet<String> hs = new HashSet<String>();
    HashMap<String,Integer> hm = new HashMap<String,Integer>();
    
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        int val;
        for(int i=0;i<participant.length;i++){
            hs.add(participant[i]);
            if(!hm.containsKey(participant[i])){
                hm.put(participant[i],1);
            }
            else{
                val=hm.get(participant[i]);
                hm.put(participant[i],val+1);
            }
        }
        
        for(int i=0;i<completion.length;i++){
            if(hm.get(completion[i])>1){
                val=hm.get(completion[i]);
                hm.put(completion[i],val-1);
            }
            else{
                hs.remove(completion[i]);
            }
        }
        
        Iterator<String> iter = hs.iterator();
        while(iter.hasNext()) answer=iter.next();
        return answer;
    }
}
