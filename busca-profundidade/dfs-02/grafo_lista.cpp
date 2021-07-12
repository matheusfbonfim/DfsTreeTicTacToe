// Grafos - Lista de adjacencia 

#include <iostream>
#include <list>
#include <algorithm> // Função find

using namespace std;

class Grafo {
  int V; // número de vertices

  // Para cada vertice teremos uma lista para seus vizinhos
  list<int> *adj; // Ponteiro para um array contendo as listas de adjacencias

  public:
      Grafo(int v); // Construtor
      void adicionaAresta(int v1, int v2); // Adiciona uma aresta no grafo

      // obtem o grau de saida de um dado vertice
      // grau de saída é o número de arcos que saem de 'v'
      int obterGrauDeSaida(int v);

      bool existeVizinho(int v1, int v2); // Verifica se v2 é vizinho de v1
};

Grafo::Grafo(int V){

  this->V = V; // Atribuindo o numero de vertices
  
  adj = new list<int>[V]; // cria as listas
}

void Grafo::adicionaAresta(int v1, int v2){
  // Adiciona vertice v2 a lista de vertices adjacentes de v1 
  adj[v1].push_back(v2);
}

int Grafo::obterGrauDeSaida(int v){
  // Tamanho da lista que é a quantidade de vizinhos
  return (adj[v]).size();
}

bool Grafo:: existeVizinho(int v1, int v2){
  if (find(adj[v1].begin(), adj[v1].end(), v2) != adj[v1].end()) {
    return true;
  }else{
    return false;
  }
}

// ============================================================================

int main(){

  // Criando um grafo de 4 vertices
  Grafo grafo(4);

  // Adicionando as arestas
  grafo.adicionaAresta(0, 1);
  grafo.adicionaAresta(0, 3);
  grafo.adicionaAresta(1, 2);
  grafo.adicionaAresta(3, 1);
  grafo.adicionaAresta(3, 2);

  // Mostrando os graus de saida
  cout << "Grau de saida do vertice 1: " << grafo.obterGrauDeSaida(1) << endl; 
  cout << "Grau de saida do vertice 3: " << grafo.obterGrauDeSaida(3) << endl; 

  // Verifica se existe vizinho
  if(grafo.existeVizinho(0, 1)){
    cout <<"1 é vizinho do 0" << endl;
  }else{
    cout <<"1 não é vizinho do 0" << endl;
  }

  return 0;
}