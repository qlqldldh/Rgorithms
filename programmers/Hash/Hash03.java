// Programmers - Hash - 위장

import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

public class Solution {
	HashMap<String, Integer> hm = new HashMap<String, Integer>();
	HashSet<String> hs = new HashSet<String>();
	
	public int solution(String[][] clothes) {
		int answer = 1;int val;
		for (int i = 0; i < clothes.length; i++) {
			if (!hm.containsKey(clothes[i][1])) {
				hm.put(clothes[i][1],1);
				hs.add(clothes[i][1]);
			} else {
				val=hm.get(clothes[i][1]);
				hm.put(clothes[i][1], val+1);
			}
		}

		Iterator<String> iter = hs.iterator();
		
		while(iter.hasNext()) {
			answer*=(hm.get(iter.next())+1);
		}
		
		return answer - 1;
	}
}
