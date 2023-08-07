import random

def adivinhar(valor):
    numero_resposta = random.randint(1, valor)
    adivinhar = 0
    
    while adivinhar != numero_resposta:
        adivinhar = int(input(f'Entre com um número entre 1 e {valor}: '))
        if adivinhar < numero_resposta:
            print('O número correto é maior que o número informado')
        elif adivinhar > numero_resposta:
            print('O número correto é menor que o número informado')

    print(f'Parabéns! Você acertou o número que é {numero_resposta}')
    return 1  # Retorna 1 ponto ao jogador

def adivinhacpu(valor, numero_resposta):
    minimo = 1
    maximo = valor
    dica = " "
    
    while dica != "Correto":
        numero_palpite = random.randint(minimo, maximo)
        print(f"A CPU chuta {numero_palpite}.")
        
        if numero_palpite < numero_resposta:
            dica = "maior"
        elif numero_palpite > numero_resposta:
            dica = "menor"
        else:
            dica = "correto"
        
        if dica == "maior":
            print("A CPU acha que o número é maior.")
            minimo = numero_palpite + 1
        elif dica == "menor":
            print("A CPU acha que o número é menor.")
            maximo = numero_palpite - 1
        elif dica == "correto":
            print("A CPU acertou!")
            return 1  # Retorna 1 ponto à CPU
    
    return 0

def jogo_adivinhacao(valor_maximo, rodadas):
    pontos_jogador = 0
    pontos_cpu = 0
    
    for rodada in range(rodadas):
        numero_resposta = random.randint(1, valor_maximo)
        print(f"\nRodada {rodada + 1}")
        
        pontos_jogador += adivinhar(valor_maximo)
        print(f"Placar - Jogador: {pontos_jogador}, CPU: {pontos_cpu}")
        
        numero_resposta = random.randint(1, valor_maximo)
        pontos_cpu += adivinhacpu(valor_maximo, numero_resposta)
        print(f"Placar - Jogador: {pontos_jogador}, CPU: {pontos_cpu}")
    
    if pontos_jogador > pontos_cpu:
        print("Você venceu!")
    elif pontos_cpu > pontos_jogador:
        print("A CPU venceu!")
    else:
        print("Empate!")

valor_maximo = int(input("Digite o valor máximo para adivinhação: "))
rodadas = 10  # Número de rodadas

jogo_adivinhacao(valor_maximo, rodadas)
