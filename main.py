import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv("resultados.csv")

# Converter colunas para tipos corretos
df["Tempo"] = pd.to_numeric(df["Tempo"])
df["Comparacoes"] = pd.to_numeric(df["Comparacoes"])
df["Trocas"] = pd.to_numeric(df["Trocas"])
df["Tamanho"] = df["Tamanho"].astype(str)  # para facilitar nos gráficos

# Estilo dos gráficos
sns.set(style="whitegrid")

# 1. Tempo de execução
g1 = sns.catplot(
    data=df, kind="bar",
    x="Tamanho", y="Tempo", hue="Algoritmo",
    col="Distribuicao", height=5, aspect=1.3
)
g1.set_axis_labels("Tamanho da Lista", "Tempo (ms)")
g1.set_titles("{col_name}")
plt.suptitle("Tempo de Execução dos Algoritmos", y=1.05)
plt.tight_layout()
plt.savefig("tempo_execucao.png")

# 2. Número de Comparações
g2 = sns.catplot(
    data=df, kind="bar",
    x="Tamanho", y="Comparacoes", hue="Algoritmo",
    col="Distribuicao", height=5, aspect=1.3
)
g2.set_axis_labels("Tamanho da Lista", "Número de Comparações")
g2.set_titles("{col_name}")
plt.suptitle("Comparações por Algoritmo", y=1.05)
plt.tight_layout()
plt.savefig("comparacoes.png")

# 3. Número de Trocas
g3 = sns.catplot(
    data=df, kind="bar",
    x="Tamanho", y="Trocas", hue="Algoritmo",
    col="Distribuicao", height=5, aspect=1.3
)
g3.set_axis_labels("Tamanho da Lista", "Número de Trocas")
g3.set_titles("{col_name}")
plt.suptitle("Trocas por Algoritmo", y=1.05)
plt.tight_layout()
plt.savefig("trocas.png")

print("Gráficos salvos com sucesso!")
