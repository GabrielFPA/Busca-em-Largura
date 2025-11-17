from collections import deque

class Grafo:
    def __init__(self):
        self.adj = {}  

    def adicionar_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def adicionar_aresta(self, u, v):
        """Grafo não direcionado"""
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs_menor_caminho(self, inicio, alvo):
        if inicio not in self.adj or alvo not in self.adj:
            return None

        fila = deque([inicio])
        visitado = {inicio}
        pai = {inicio: None}

        while fila:
            atual = fila.popleft()

            if atual == alvo:
                return self._reconstruir_caminho(pai, alvo)

            for vizinho in self.adj[atual]:
                if vizinho not in visitado:
                    visitado.add(vizinho)
                    pai[vizinho] = atual
                    fila.append(vizinho)

        return None  

    def _reconstruir_caminho(self, pai, alvo):
        caminho = []
        atual = alvo
        while atual is not None:
            caminho.append(atual)
            atual = pai[atual]
        caminho.reverse()
        return caminho

    def mostrar_grafo(self):
        print("\n=== Lista de Adjacência do Grafo ===")
        for vertice, vizinhos in self.adj.items():
            print(f"{vertice} -> {vizinhos}")
        print("====================================\n")




def main():
    grafo = Grafo()

    print("===== CONSTRUÇÃO DO GRAFO =====")
    
    while True:
        print("\n1 - Adicionar aresta")
        print("2 - Mostrar grafo")
        print("3 - Buscar menor caminho (BFS)")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            u = input("Digite o primeiro vértice: ").strip()
            v = input("Digite o segundo vértice: ").strip()
            grafo.adicionar_aresta(u, v)
            print(f"Aresta adicionada: {u} <-> {v}")

        elif opcao == "2":
            grafo.mostrar_grafo()

        elif opcao == "3":
            inicio = input("Vértice inicial: ").strip()
            alvo = input("Vértice final: ").strip()
            caminho = grafo.bfs_menor_caminho(inicio, alvo)

            if caminho:
                print(f"\nMenor caminho encontrado: {caminho}\n")
            else:
                print("\nNão existe caminho entre esses vértices.\n")

        elif opcao == "4":
            print("Encerrando...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()