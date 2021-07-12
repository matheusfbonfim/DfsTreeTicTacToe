#include<iostream>
#include<iterator> // for iterators
#include<vector> // for vectors
#include<stack>

using namespace std;

const int N = 8;
vector<int> adj[N];
vector<bool> visited;

void dfs(int u){
  // A partir da raiz, marca como visitado
  visited[u] = true;
  // cout << u << ' ';

  for(auto v: adj[u]){
    cout << "\n" << v << ' '<< "\n\n";

    if(!visited[v]){
      dfs(v);
    }
  }
}

void dfsStack(int u){
  stack<int> s;

  s.push(u);

  while(!s.empty()){
    int v = s.top();
    s.pop();

    cout << v << ' ';

    visited[v] = true;

    for (auto e : adj[v]){
      if(!visited[e]){
        s.push(e);
      }
    }
  }

}


int main(){

  
  visited.assign(N, false);

  // for (vector<int>::iterator it = visited.begin(); it != visited.end(); it++){
  //    cout << *it << " "; // valor na posição apontada por it
  // } 

  adj[0].push_back(1);
  adj[0].push_back(2);
  adj[1].push_back(3);
  adj[3].push_back(4);
  adj[4].push_back(6);
  adj[2].push_back(5);
  adj[5].push_back(7);

  cout << '\n';

  // for (vector<int>::iterator it = adj[3].begin(); it != adj[3].end(); it++) {
  //   cout << *it << " "; // valor na posição apontada por it
  // } 

  dfsStack(0);

  return 0;
}

