# 📊 Análise Empírica de Algoritmos de Ordenação

Este projeto consiste em uma análise comparativa teórica e prática de seis algoritmos clássicos de ordenação, avaliando desempenho em diferentes tamanhos e distribuições de dados.

## 🧠 Algoritmos Avaliados

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

## 🎯 Objetivos

- Implementar os algoritmos de ordenação.
- Analisar suas complexidades assintóticas.
- Medir tempo de execução, número de comparações e trocas.
- Avaliar desempenho em diferentes distribuições de entrada: ordenada, inversa e aleatória.
- Produzir gráficos e tabelas com os resultados.

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- `pandas`
- `matplotlib`
- `time` (para mensuração)
- `random` (geração de listas)
- `csv` (exportação de dados)
- `Git` para controle de versão
- [**LaTeX com UFTex**](https://github.com/almeidatiago/UFTeX) para o relatório técnico

## 📁 Estrutura do Projeto

AEAO/
├── algoritmos.py # Implementações dos algoritmos com contadores de métricas
├── testes.py # Script principal que executa os testes
├── resultados.csv # Resultados consolidados das execuções
├── graficos.py # Geração dos gráficos com matplotlib
├── README.md # Este arquivo
└── relatorio/ # (Opcional) Relatório em LaTeX com UFTex


## ▶️ Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/devdinho/AEAO.git
    cd AEAO
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute os testes:
    ```bash
    python testes.py
    ```

4. Gere os gráficos (opcional):
    ```bash
    python graficos.py
    ```

## 📈 Métricas Coletadas
#### ⏱️ Tempo de execução (ms)
#### 🔁 Número de comparações
#### 🔃 Número de trocas

## 👨‍🏫 Relatório
O relatório técnico foi elaborado com base nos dados gerados por este projeto e está disponível em LaTeX utilizando o modelo institucional [**UFTex**](https://github.com/almeidatiago/UFTeX).

## 👥 Autores
Anderson Freitas [@devdinho](https://github.com/devdinho)