def inverter_vetor(vetor):
    vetor_invertido = vetor[::-1] # inverte usando a técnica de fatiamento
    return vetor_invertido

if __name__ == "__main__":
    try:
        tamanho_vetor = int(input("Digite o tamanho do vetor: "))
        vetor = []

        for i in range(tamanho_vetor):
            valor = int(input(f"Digite o {i+1}º valor: "))
            vetor.append(valor) #O método append insere os numeros lidos
            # na variável valor dentro do vetor criado (pode ser feito em
            # lista também)

        vetor_invertido = inverter_vetor(vetor)

        print("Vetor invertido: ", vetor_invertido)
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar valores numéricos.")
