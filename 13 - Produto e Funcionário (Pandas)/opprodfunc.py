import pandas as pd
import plotly.express as px

# Carregar os CSVs
df_produtos = pd.read_csv("tabelaproduto.csv", sep=";", encoding="ISO-8859-1")
df_funcionarios = pd.read_csv("tabelafuncionario.csv", sep=";", encoding="ISO-8859-1")

# Mostrar os cargos que ganham mais em um gráfico
fig = px.bar(df_funcionarios, x="Salario", y="Cargo", orientation="h", title="Média Salarial por Cargo")
fig.update_layout(xaxis_title="Salário (R$)", yaxis_title="Cargo")
fig.show()
fig.write_image("grafico_salarios.png")

# Mostrar os produtos mais caros pro mais barato em um gráfico
fig = px.bar(df_produtos.sort_values(by="Preco", ascending=False), x="Preco", y="NomeProduto", orientation="h", title="Preço dos Produtos")
fig.update_layout(xaxis_title="Preço (R$)", yaxis_title="Produto")
fig.show()
fig.write_image("grafico_precos.png")