// programmers - 2017 팁스타운 - 예상 대진표

public class Solution4 {
	int nextSeq(int m) {
		return m%2==0?m/2:(m+1)/2;
	}
	
	public int solution(int n, int a, int b) {
		int answer = 1;

		while(Math.abs(a-b)!=1 || Math.max(a, b)%2!=0) {
			a=nextSeq(a);
			b=nextSeq(b);
			answer+=1;
		}

		return answer;
	}
}
