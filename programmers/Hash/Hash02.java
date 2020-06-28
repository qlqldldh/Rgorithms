// Programmers - Hash - 전화번호 목록

import java.util.HashSet;

public class Solution {
	HashSet<String> hs = new HashSet<String>();

	public boolean solution(String[] phone_book) {
		boolean answer = true;
		for (int i = 0; i < phone_book.length; i++) {
			if (!hs.contains(phone_book[i])) {
				hs.add(phone_book[i]);
			} else {
				return false;
			}
		}
		String str;
		for(int i=0;i<phone_book.length;i++) {
			str="";
			for(int j=0;j<phone_book[i].length()-1;j++) {
				str+=phone_book[i].charAt(j);
				if(hs.contains(str)) return false; 
			}
		}
		
		return true;
	}
}
