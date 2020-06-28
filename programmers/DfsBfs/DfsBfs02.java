// Programmers - DFS/BFS - 네트워크

#include <string>
#include <vector>
#include <queue>
using namespace std;

queue<int> pnts;
vector<bool> flags;

int Answer;

void bfs(vector<vector<int>> cmp){
    if(pnts.empty()){
        Answer+=1;
        return;
    }
    int sz=pnts.size();
    for(int i=0;i<sz;i++){
        for(unsigned int j=0;j<cmp.size();j++){
            if(cmp[pnts.front()][j]==1 && flags[j]==false){
                pnts.push(j);
                flags[j]=true;
            }
        }
        pnts.pop();
    }
    bfs(cmp);
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    for(unsigned int i=0;i<computers.size();i++){
        flags.push_back(false);
    }
    
    for(unsigned int i=0;i<computers.size();i++){
        if(flags[i]==false){
            pnts.push(i);
            bfs(computers);
        }
    }
    answer=Answer;
    return answer;
}
