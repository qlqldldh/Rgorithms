// Programmers - DP - 타일 장식물 

class Solution {
    
    public long solution(int N) {
        long answer = 0;
        long[] dp = new long[2];
        dp[0]=1; // rows
        dp[1]=1; // cols
        
        for(int i=2;i<=N;i++){
            if(i%2==0){
                dp[0]+=dp[1];
            }
            else{
                dp[1]+=dp[0];
            }
        }
        answer=2*(dp[0]+dp[1]);
        return answer;
    }
}
