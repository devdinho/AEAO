import csv
import time
import random
from algoritmos import *

algoritmos = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}

tamanhos = [1000, 10000, 50000, 100000]
distribuicoes = ["Aleatoria", "Ordenada", "Inversa"]

def gerar_lista(tamanho, tipo):
    if tipo == "Aleatoria":
        return random.sample(range(tamanho*2), tamanho)
    elif tipo == "Ordenada":
        return list(range(tamanho))
    elif tipo == "Inversa":
        return list(range(tamanho, 0, -1))

with open("resultados.csv", "w", newline="") as csvfile:
    fieldnames = ["Algoritmo", "Tamanho", "Distribuicao", "Tempo", "Comparacoes", "Trocas"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for tamanho in tamanhos:
        for dist in distribuicoes:
            lista_base = gerar_lista(tamanho, dist)
            for nome, funcao in algoritmos.items():
                lista = lista_base.copy()
                stats = {"comparacoes": 0, "trocas": 0}
                inicio = time.perf_counter()
                if nome == "Merge Sort":
                    funcao(lista, stats)  # recebe e retorna
                else:
                    funcao(lista, stats)  # in-place
                fim = time.perf_counter()
                tempo_ms = (fim - inicio) * 1000

                writer.writerow({
                    "Algoritmo": nome,
                    "Tamanho": tamanho,
                    "Distribuicao": dist,
                    "Tempo": round(tempo_ms, 3),
                    "Comparacoes": stats["comparacoes"],
                    "Trocas": stats["trocas"]
                })
                print(f"{nome} - {tamanho} - {dist}: OK")
