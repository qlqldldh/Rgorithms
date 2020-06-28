// Programmers - DP - 정수 삼각형 

class Solution {
    int Max(int n1, int n2){
        return n1>n2?n1:n2;
    }
    
    public int solution(int[][] triangle) {
        int[][] dp= new int[triangle.length][triangle.length];
        int answer=0;
        
        dp[0][0]=triangle[0][0];
        for(int i=1;i<triangle.length;i++){
            for(int j=0;j<triangle[i].length;j++){
                if(j==0){
                    dp[i][j]=triangle[i][j]+dp[i-1][j];
                }
                else if(j==triangle[i].length-1){
                    dp[i][j]=triangle[i][j]+dp[i-1][j-1];
                }
                else{
                    dp[i][j]=Max(dp[i-1][j],dp[i-1][j-1])+triangle[i][j];
                }
            }
        }
        for(int i=0;i<triangle.length;i++){
            answer=Max(answer,dp[triangle.length-1][i]);
        }
        
        return answer;
    }
}
