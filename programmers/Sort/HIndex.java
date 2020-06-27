// Programmers - Sort - H-Index

import java.util.Arrays;

class Solution {
	public int solution(int[] citations) {
		Arrays.sort(citations);
		int h = 0;
		int index=0;
		
		for(h=0;h<10001;h++) {
			if(citations[index]==h) {
				while(index<citations.length && citations[index]==h)index++;
			}
			if(citations.length-index<=h) break;
		}
		
		return h;
	}

}
