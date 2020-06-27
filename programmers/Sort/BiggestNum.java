package actualTest;

// n = (int) (Math.random() * 20); //

import java.util.Comparator;
import java.util.Arrays;

class BiggestNum {
	public String solution(int[] numbers) {
		String[] strNums = new String[numbers.length];
		for(int i=0;i<numbers.length;i++) strNums[i]=Integer.toString(numbers[i]);
		
		Arrays.sort(strNums,new Comparator<String>(){

			@Override
			public int compare(String n1, String n2) {
				// TODO Auto-generated method stub
				return Integer.parseInt(n2+n1) - Integer.parseInt(n1+n2);
			}
			
		});
		StringBuffer sb = new StringBuffer();
		for(int i=0;i<strNums.length;i++) {
			sb.append(strNums[i]);
		}
		
		return sb.toString();
	}
	
	public static void main(String[] args) {
		BiggestNum s = new BiggestNum();
		int[] nums = {3,30,34,5,9};
		
		System.out.println(s.solution(nums));
		
	}
}