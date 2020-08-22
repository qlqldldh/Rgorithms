// programmers - 2017 팁스타운 - 짝지어 제거하기

class Solution2 {
	public int solution(String s) {
		int answer = 0;
		
		StringBuffer sb = new StringBuffer();
		
		int sbLength;
		sb.append(s.charAt(0));
		for(int i=1;i<s.length();i++) {
			sbLength=sb.length();
			if(sbLength!=0 && sb.charAt(sbLength-1)==s.charAt(i)) {
				sb.deleteCharAt(sbLength-1);
			} else {
				sb.append(s.charAt(i));
			}
		}
		

		return sb.length()==0?1:0;
	}
	
	public static void main(String[] args) {
		Solution2 ss = new Solution2();
		
//		System.out.println(ss.solution("baabaa"));
	}
}
