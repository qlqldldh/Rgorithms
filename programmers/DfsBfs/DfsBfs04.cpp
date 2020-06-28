// Programmers - DFS/BFS - 여행경로 

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<bool> flags;
vector<string> Answer;

void dfs(vector<vector<string>> tk, vector<string> &ans, string srt, int cnt){
    if(cnt==tk.size()){
        for(int i=0;i<=cnt;i++){
            ans.push_back(Answer[i]);
        }
        return;
    }
    
    for(unsigned int i=0;i<tk.size();i++){
        if(flags[i]==false && srt==tk[i][0]){
            flags[i]=true;
            Answer.push_back(tk[i][1]);
            dfs(tk,ans,tk[i][1],cnt+1);
            Answer.pop_back();
            flags[i]=false;
        }
    }
}


vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    vector<string> aans;
    sort(tickets.begin(),tickets.end());
    
    for(unsigned int i=0;i<tickets.size();i++)
        flags.push_back(false);
    
    Answer.push_back("ICN");
    
    dfs(tickets,aans,"ICN",0);
    
    for(unsigned int i=0;i<=tickets.size();i++)
        answer.push_back(aans[i]);
    
    return answer;
}
