// Programmers - Stack And Queue - 탑

class Solution {
    public int[] solution(int[] heights) {
        int[] answer = new int[heights.length];
        boolean sig;
        
        for(int i=heights.length-1;i>=0;i--){
            sig=false;
            for(int j=i-1;j>=0;j--){
                if(heights[i]<heights[j]){
                    answer[i]=j+1; sig=true; break;
                }
            }
            if(!sig) answer[i]=0;
        }
        
        return answer;
    }
}
