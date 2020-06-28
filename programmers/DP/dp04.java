// Programmers - DP - 등굣길 

class Solution {
    int[][] dp;
    final int _mod=1000000007;
    
    public int solution(int m, int n, int[][] puddles) {
        dp=new int[n+1][m+1];
        boolean[][] pond = new boolean[n+1][m+1];

        for(int i=0;i<puddles.length;i++){
            pond[puddles[i][1]][puddles[i][0]]=true;
        }
        
        dp[1][0]=1;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                if(!pond[i][j]) dp[i][j]=(dp[i][j-1]+dp[i-1][j])%_mod;
                else dp[i][j]=0;
            }
        }
        
        return dp[n][m];
    }
}
