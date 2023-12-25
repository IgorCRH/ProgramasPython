from pathlib import Path
import pandas as pd
import pytz

HERE = Path(__file__).parent

caminho_alunos = r"C:\Users\lar\Desktop\UFRRJMaterias\Linguagens\Python\13 - Projeto Panda\tabelaalunos.csv"

carregaralunos = pd.read_csv(
    caminho_alunos,
    converters={"Matricula": str.lower, "Email": str.lower},
    sep=";",
    usecols=["Matricula", "Email", "Secao"],
    index_col="Matricula"
)

carregartarefa = pd.read_csv(
    HERE / "tabelatarefas.csv",
    converters={"Matricula": str.lower},
    usecols=lambda x: "Entrega" not in x,
    index_col="Matricula"
)

carregargrades = pd.read_csv(
    HERE / "tabelagrades.csv",
    converters={"Email": str.lower},
    usecols=lambda x: "Entrega" not in x,
    index_col="Matricula"
)

nivel_testes = pd.DataFrame()

file_pattern = "testes.csv"
carregartarefa["Tarefa 1"] = pd.to_numeric(carregartarefa["Tarefa 1"], errors='coerce')

for file_path in HERE.glob(file_pattern):
    
    nome_teste = " ".join(file_path.stem.title().split("_")[:3])
    
    carregar_testes = pd.read_csv(
        file_path,
        converters={"Email": str.lower},
        index_col=["Email"],
        usecols=["Email", "Nivel"],
    ).rename(columns={"Nivel": nome_teste})
    
    nivel_testes = pd.concat([nivel_testes, carregar_testes], axis=1)

mergealunostarefa = pd.merge(
    carregaralunos, carregartarefa, left_index=True, right_index=True
)

dadosfinais = pd.merge(
    mergealunostarefa, carregargrades, nivel_testes, left_index=True, right_index=True
)

dadosfinais = dadosfinais.fillna(0)

numerotestes = 6

for n in range(1, numerotestes + 1):
    dadosfinais[f"Teste{n} Pontuação:"] = (
        dadosfinais[f"Exame {n}"] / dadosfinais[f"Exame {n} - Pontuacao Maxima"]
    )

tarefa_pontuacao = dadosfinais.filter(regex=r"^Tarefa \d\d?$", axis=1)

tarefa_max_pontuacao = dadosfinais.filter(regex=r"^Tarefa \d\d? -", axis=1)

for coluna_tarefa, coluna_max_pontos in zip(tarefa_pontuacao.columns, tarefa_max_pontuacao.columns):
    numero_tarefa = coluna_tarefa.split(" ")[-1]
    dadosfinais[f"Tarefa {numero_tarefa} Pontuação"] = (
        dadosfinais[coluna_tarefa] / dadosfinais[coluna_max_pontos]
    )

print(dadosfinais)

soma_tarefa_max_pontuacao = tarefa_pontuacao.sum(axis=1)

soma_tarefa_pontuacao = tarefa_max_pontuacao.sum(axis=1)

dadosfinais["Pontuacao Tarefa"] = dadosfinais[
    ["Pontuacao Total", "Pontuacao Media"]
].max(axis=1)
