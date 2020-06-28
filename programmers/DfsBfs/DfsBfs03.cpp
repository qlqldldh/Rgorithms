// Programmers - DFS/BFS - 단어변환 

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int Answer;

vector<bool> flags;

bool compare_word(string b, string t){
    int cnt=0;
    for(int i=0;i<b.length();i++){
        if(b[i]!=t[i])
            cnt+=1;
    }
    if(cnt==1)
        return true;
    else
        return false;
}

void dfs(vector<string> wd, string bg, string tg, int cnt){
    if(bg==tg){
        Answer=min(Answer,cnt);
        return;
    }
    for(int i=0;i<wd.size();i++){
        if(compare_word(bg,wd[i]) && flags[i]==false){
            flags[i]=true;
            dfs(wd,wd[i],tg,cnt+1);
            flags[i]=false;
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    Answer=987654;
    for(unsigned int i=0;i<words.size();i++)
        flags.push_back(false);
    
    dfs(words,begin,target,0);
    if(Answer!=987654)
        answer=Answer;
    
    return answer;
}
