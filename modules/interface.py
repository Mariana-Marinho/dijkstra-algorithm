from modules import dijkstra
import tkinter as tk
from tkinter import ttk

def criar_interface_grafica(grafo):
    def encontrar_melhor_caminho():
        vertice_inicial = origem_entry.get()
        vertice_final = destino_entry.get()

        if vertice_inicial not in grafo or vertice_final not in grafo:
            resultado_label.config(text="E-mail de origem OU E-mail de destino inválidos na nossa emails_universitarios.txt de dados.")
            return

        caminho, peso = ecmin.encontrar_caminho_minimo(vertice_inicial, vertice_final)

        caminho_formatado = "\n".join(
            f"{caminho[i]} --> {caminho[i + 1]} (peso {grafo[caminho[i]][caminho[i + 1]]})" for i in
            range(len(caminho) - 1))
        resultado_label.config(text=f'MELHOR CAMINHO:\n{caminho_formatado}\nTOTAL DOS PESOS DO CAMINHO: {peso}\nFIM')

    ecmin = dijkstra.EncontradorCaminhoMinimo(grafo)

    root = tk.Tk()
    root.title("DIJKSTRA")
    root.configure(bg="#f0f0f0")

    frame = ttk.Frame(root, padding=20)
    frame.pack()

    style = ttk.Style()
    style.configure("TButton", background="#4287f5")

    origem_label = ttk.Label(frame, text="E-mail de origem:", foreground="#333333", background="#f0f0f0")
    origem_label.grid(row=0, column=0, sticky="w")

    origem_entry = ttk.Entry(frame)
    origem_entry.grid(row=0, column=1)

    destino_label = ttk.Label(frame, text="E-mail de destino:", foreground="#333333", background="#f0f0f0")
    destino_label.grid(row=1, column=0, sticky="w")

    destino_entry = ttk.Entry(frame)
    destino_entry.grid(row=1, column=1)

    calcular_button = ttk.Button(frame, text="Encontre o melhor caminho e os pesos", command=encontrar_melhor_caminho)
    calcular_button.grid(row=2, columnspan=2, pady=10)

    resultado_label = ttk.Label(frame, text="", justify="left", foreground="#333333", background="#f0f0f0")
    resultado_label.grid(row=3, columnspan=2, pady=10)

    root.mainloop()