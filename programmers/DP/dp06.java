// Programmers - DP - 도둑질

class Solution {
    int Max(int n1, int n2){
        return n1>n2?n1:n2;
    }
    
    public int solution(int[] money) {
        int[] dpFirst = new int[money.length];
        int[] dpLast = new int[money.length];
        
        dpFirst[0]=money[0]; dpFirst[1]=Max(money[1],dpFirst[0]);
        dpLast[0]=0; dpLast[1]=money[1];
        
        for(int i=2;i<money.length;i++){
            dpFirst[i]=Max(dpFirst[i-1],dpFirst[i-2]+money[i]);
        }
        dpFirst[money.length-1] = dpFirst[money.length-2];
        for(int i=2;i<money.length;i++){
            dpLast[i]=Max(dpLast[i-1],dpLast[i-2]+money[i]);
        }        
        
        return Max(dpFirst[money.length-1],dpLast[money.length-1]);
    }
}
