// Grafos - DFS - BUSCA EM PROFUNDIDADE 

#include <iostream>
#include <list>
#include <algorithm> // Função find
#include <stack> // Pilha para usar na DFS

using namespace std;

class Grafo {
  int V; // número de vertices

  // Para cada vertice teremos uma lista para seus vizinhos
  list<int> *adj; // Ponteiro para um array contendo as listas de adjacencias

  public:
    Grafo(int v); // Construtor
    void adicionaAresta(int v1, int v2); // Adiciona uma aresta no grafo
    
    // Faz uma DFS a partir de um vertice 
    void dfs(int v);
};


// CONSTRUTOR
Grafo::Grafo(int V){

  this->V = V; // Atribuindo o numero de vertices
  
  adj = new list<int>[V]; // cria as listas
}

// ADICIONANDO ARESTAS
void Grafo::adicionaAresta(int v1, int v2){
  // Adiciona vertice v2 a lista de vertices adjacentes de v1 
  adj[v1].push_back(v2);
}

// DFS
void Grafo::dfs(int v){
  stack<int> pilha;
  bool visitados[V]; // Vetor de visitados

  // Marcar todos como não visitados
  for(int i = 0; i < V; i++){
    visitados[i] =  false;
  }

  while(true){

    if(!visitados[v]){

        cout<< "Visitando o vertice: " << v << "....\n";
        visitados[v] = true; // marca como visitado
        pilha.push(v); // "Insere v na pilha"
    }

    bool achou = false;
    // Iremos iterar na lista
    list<int>::iterator it;

    // busca por um vizinho nao visitado
    for(it = adj[v].begin(); it != adj[v].end(); it++){
      
      if(!visitados[*it]){
        achou = true;
        break;
      }
    }

    if(achou){
      v = *it; // atualiza o "v"
    }else{
      // se todos os vizinhos estão visitados ou não existem vizinhos
      // remove da pilha
      pilha.pop(); 
      // se a pilha ficar vazia, então terminou a busca
      if (pilha.empty()){
        break;
      }
      // se chegou aqui é porque pegar o elemento do topo
      v = pilha.top();
    }

  }
}

// ============================================================================

int main(){

  int V = 8;

  // Criando um grafo de 8 vertices
  Grafo grafo(8);

  // Adicionando as arestas
  grafo.adicionaAresta(0, 1);
  grafo.adicionaAresta(0, 2);
  grafo.adicionaAresta(1, 3);
  grafo.adicionaAresta(1, 4);
  grafo.adicionaAresta(2, 5);
  grafo.adicionaAresta(2, 6);
  grafo.adicionaAresta(6, 7);

  grafo.dfs(0);

  return 0;
}