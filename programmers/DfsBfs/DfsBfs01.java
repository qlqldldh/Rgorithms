// Programmers - DFS/BFS - 타겟넘버 

#include <string>
#include <vector>

using namespace std;


void dfs(vector<int> nums, int indx,int sum,int tgt,int* ans){
    if(indx==nums.size()-1){
        
        if(sum+nums[indx]==tgt)
            *ans+=1;
        else if(sum-nums[indx]==tgt)
            *ans+=1;
        return;
    }
    dfs(nums,indx+1,sum-nums[indx],tgt, ans);
    dfs(nums,indx+1,sum+nums[indx],tgt,ans);
    
}

int solution(vector<int> numbers, int target) {
    int answer=0;
    
    dfs(numbers,0,0,target,&answer);
    //dfs(numbers,0,0,target,&answer);
    
    
    return answer;
}
