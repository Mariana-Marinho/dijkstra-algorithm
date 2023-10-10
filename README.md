# Projeto de Visualização de Grafos com Dijkstra

## Contexto do Problema

**Contexto:** Imagine que você é responsável pelo setor de TI de uma universidade. Você recebeu a tarefa de desenvolver uma ferramenta que permita encontrar o menor caminho entre dois endereços de e-mail dos alunos da universidade. Isso é especialmente útil para otimizar a comunicação entre os alunos e garantir que informações importantes sejam transmitidas da maneira mais eficiente possível.

Para resolver esse desafio, este projeto utiliza o algoritmo de Dijkstra para calcular o menor caminho entre os vértices do grafo, representando os endereços de e-mail dos alunos. A interface gráfica permite aos usuários inserir os endereços de e-mail de origem e destino, e em seguida, o algoritmo de Dijkstra calcula o caminho mais curto entre esses pontos.

**Base de Dados:**  E-mail network URV dataset.

**Conteúdo:** A base contém nós, variando de 1 a 1133, a conexão entre nós e o peso da aresta, no formato (nó conexão peso). O peso original entre quaisquer vértices era de 1, por esse motivo randomizamos pesos entre 1 e 15 para variá-lo.

**Discentes:** Aldo dos Santos Ferreira Lemos (asfl) e Mariana Marinho da Silva Andrade (mmsa).
## Implementação

**Algoritmo Utilizado:** Dijkstra
**Desenvolvimento:** O arquivo é dividido entre as pastas 'data-base' e 'modules', contendo respectivamente a base de dados e os códigos da interface, algoritmo, função para mudança da base de dados e setup para instalar as bibliotecas necessárias, e o código main. 
- alter_database.py contém uma função que randomiza os pesos entre nós na base de dados. 
- dijkstra.py contém a classe do algoritmo dijkstra. 
- interface.py contém as funções para a interface.
- setup.py instala as bibliotecas necessárias para o projeto rodar
- main.py importa todos esses arquivos e é a partir dele que o código é rodado.

```
dijkstra-algorithm
├── README.md
├── data_base
|  └── database.txt
├── main.py
└── modules
   ├── alter_database.py
   ├── dijkstra.py
   ├── interface.py
   └── setup.py
```

## Como rodar o projeto
1. Após rodar o código main, digite os nós na interface e veja o caminho mais curto entre eles:
    <img src=".\assets\exemplo_1.jpeg" />
2. Aguarde a vizualização do grafo com o caminho entre os nós destacado em vermelho:
    <img src=".\assets\grafo_1.1.jpeg" />
3. Dê zoom no gráfico para melhor vizualizar o caminho:
    <img src=".\assets\grafo_1.2.jpeg" />

## Bibliotecas Utilizadas

-  `matplotlib.pyplot`: Usada para criar visualizações gráficas do grafo e destacar as rotas calculadas.
- `random`: Gera números aleatórios para o peso das arestas.
- `tkinter`: Cria a interface gráfica para inserção dos vértices de origem e destino.
- `networkx`: Utilizada para representar o grafo em memória, calcular o menor caminho e criar visualizações gráficas.
- `subprocess`: Usada para instalar as bibliotecas necessárias para o código automaticamente.

## Conclusão

Houve uma certa dificuldade em encontrar uma base de dados viável e em como plotá-la, além de ser necessário entender como melhor organizar o arquivo em módulos, e não somente um grande código.

## Prints de Tela

**Exemplo:**
<img src=".\assets\exemplo_2.jpeg" />
<img src=".\assets\grafo_2.1.jpeg" />
<img src=".\assets\grafo_2.2.jpeg" />


## Referências

- Guimera, R., Danon, L., Diaz-Guilera, A., Giralt, F., & Arenas, A. (2003). E-mail network URV dataset. Disponível em: https://deim.urv.cat/~alexandre.arenas/data/welcome.htm.
- Hashtag Programação. Como Criar uma Tela em Python Para Seus Códigos - [Interface Gráfica Intuitiva com Tkinter]. YouTube, 3 de julho de 2021. Disponível em: https://youtu.be/AiBC01p58oI?si=RSjDoIWHz8wNOt0c
