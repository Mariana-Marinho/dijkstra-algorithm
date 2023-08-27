from modules import alter_database, interface, dijkstra
import data_base

# altera o peso dos caminhos entre usuários
alter_database.alterar_pesos_arquivo("data_base/database.txt", 1, 15)

#carrega o grafo a partir do arquivo
grafo = {}
with open("data_base/database.txt", "r") as arquivo:
    for linha in arquivo:
        partes = linha.split()
        origem = partes[0]
        destino = partes[1]
        peso = int(partes[2])
        if origem not in grafo:
            grafo[origem] = {}
        grafo[origem][destino] = peso

#cria a interface gráfica
interface.criar_interface_grafica(grafo)
