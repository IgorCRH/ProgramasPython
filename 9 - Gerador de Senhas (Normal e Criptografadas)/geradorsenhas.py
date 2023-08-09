import random

print('Gerador de Senhas')

caracteres = 'ABCDEFGHIJLMNOPQRSTUVWXYZabcdefghijlmnopqrstuvwxyz!#@%$&*.[]'
qtdsenhas = int(input('Entre com quantas senhas deseja gerar: '))
tamanho = int(input('Entre com o tamanho desejado das senhas: '))

print('Senhas: ')
for _ in range(qtdsenhas):  # Usando "_" para indicar que não usamos a variável "senha" aqui
    senha = ''  # Corrigindo a inicialização da senha
    for _ in range(tamanho):  # Usando "_" para indicar que não usamos a variável "caracteres" aqui
        senha += random.choice(caracteres)
    print(senha)
