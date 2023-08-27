import random

def alterar_pesos_arquivo(path, minimo, maximo):
    #altera os pesos do arquivo para valores aleatórios entre 1 e 5.
    linhas_modificadas = []

    with open(path, "r") as arquivo:
        for linha in arquivo:
            partes = linha.split()
            vertice_origem = partes[0]
            vertice_destino = partes[1]
            novo_peso = random.randint(minimo, maximo)  #gera um peso aleatório entre o minimo e o maximo fornecido (altere conforme necessário)
            nova_linha = f"{vertice_origem} {vertice_destino} {novo_peso}\n"
            linhas_modificadas.append(nova_linha)

    with open(path, "w") as arquivo:
        arquivo.writelines(linhas_modificadas)
