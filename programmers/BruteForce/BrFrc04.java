// Programmers - Brute Force - 카펫 

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int total = brown+yellow;
        
        for(int i=yellow;i>=1;i--){
            if(yellow%i==0){
                if(brown==2*(i+2+yellow/i)){
                    answer[0]=i+2;
                    answer[1]=yellow/i+2;
                    break;
                }
            }
            if(i<yellow/i) break;
        }
        
        return answer;
    }
}
