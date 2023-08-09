import random
import hashlib

print('Gerador de Senhas Criptografadas')

caracteres = 'ABCDEFGHIJLMNOPQRSTUVWXYZabcdefghijlmnopqrstuvwxyz!#@%$&*.[]'
qtdsenhas = int(input('Entre com quantas senhas deseja gerar: '))
tamanho = int(input('Entre com o tamanho desejado das senhas: '))

print('Senhas Criptografadas: ')
for _ in range(qtdsenhas):
    senha = ''
    for _ in range(tamanho):
        senha += random.choice(caracteres)

    # Criando o hash da senha usando SHA-256
    sha256_hash = hashlib.sha256(senha.encode()).hexdigest()
    print(sha256_hash)
