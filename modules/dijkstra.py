#classe que implementa o algoritmo de dijkstra
class EncontradorCaminhoMinimo:
    def __init__(self, grafo):
        #inicialização das estruturas de dados para o algoritmo de Dijkstra
        self.grafo = grafo
        self.custos_minimos = {vertice: float('inf') for vertice in grafo}
        self.distancias_temporarias = {}
        self.predecessores = {}
        for vertice in grafo:
            self.distancias_temporarias[vertice] = float('inf')

    def encontrar_caminho_minimo(self, vertice_inicial, vertice_final):
        #inicialização das distâncias para o vértice inicial
        self.distancias_temporarias[vertice_inicial] = 0
        self.custos_minimos[vertice_inicial] = 0
        self.predecessores[vertice_inicial] = None

        #loop principal do algoritmo de Dijkstra
        while self.distancias_temporarias:
            #encontra o vértice com a menor distância temporária
            vertice_atual = min(self.distancias_temporarias, key=self.distancias_temporarias.get)
            del self.distancias_temporarias[vertice_atual]

            #explora os vértices adjacentes ao vértice atual
            for vertice_adjacente, peso in self.grafo[vertice_atual].items():
                #calcula a nova distância até o vértice adjacente
                nova_distancia = self.custos_minimos[vertice_atual] + peso

                #atualiza se a nova distância for menor que a distância atual
                if nova_distancia < self.custos_minimos[vertice_adjacente]:
                    self.custos_minimos[vertice_adjacente] = nova_distancia
                    self.distancias_temporarias[vertice_adjacente] = nova_distancia
                    self.predecessores[vertice_adjacente] = vertice_atual

        #constrói o caminho mínimo a partir dos predecessores
        caminho_minimo = []
        vertice_auxiliar = vertice_final
        while vertice_auxiliar is not None:
            caminho_minimo.append(vertice_auxiliar)
            vertice_auxiliar = self.predecessores[vertice_auxiliar]
        caminho_minimo.reverse()

        #retorna o caminho mínimo e o custo total
        return caminho_minimo, self.custos_minimos[vertice_final]