// Programmers - Stack And Queue - 쇠막대기 

import java.util.Stack;

class Solution {
    Stack<Character> stk = new Stack<Character>();

	public int solution(String arrangement) {
		int answer = 0;
		boolean laser=false;
		for(int i=0;i<arrangement.length();i++) {
			if(arrangement.charAt(i)=='(') {
				stk.add(arrangement.charAt(i));
				laser=true;
			}
			else {
				if(laser) {
					stk.pop();
					answer+=stk.size();
					laser=false;
				}
				else {
					stk.pop();
					answer+=1;
				}
			}
		}
		
		return answer;
	}
}
