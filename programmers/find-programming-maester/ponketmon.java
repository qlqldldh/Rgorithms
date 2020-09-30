import java.util.Arrays;

class Solution {
    public int solution(int[] nums) {
		int answer = 1;
		Arrays.sort(nums);
		
		for (int i = 1; i < nums.length; i++) {
			  if(answer==nums.length/2) break;
        if(nums[i]!=nums[i-1]) answer+=1;
		}

        return answer;
	}
}
