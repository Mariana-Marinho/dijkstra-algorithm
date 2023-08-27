from modules import alter_database, interface, dijkstra
import data_base

# altera o peso dos caminhos entre usuários
alter_database.alterar_pesos_arquivo("data_base/database.txt", 1, 15)

#carrega o grafo a partir do arquivo
grafo = {}
with open("data_base/database.txt", "r") as arquivo:
    for linha in arquivo:
        partes = linha.split()
        vertice_origem = partes[0]
        vertice_destino = partes[1]
        peso = int(partes[2])
        if vertice_origem not in grafo:
            grafo[vertice_origem] = {}
        grafo[vertice_origem][vertice_destino] = peso

#cria a interface gráfica
interface.criar_interface_grafica(grafo)
