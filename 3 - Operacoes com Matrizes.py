def preencher_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            valor = int(input("Digite um valor: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    print("Matriz:")
    for linha in matriz:
        print(linha)

def somadiagonalprincipal(matriz):
    soma = 0;
    for i in range(len(matriz)):
        soma+=matriz[i][i]

    print("Soma da diagonal principal:", soma)

def transposta(matriz):
    transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    
    print("Matriz transposta:")
    for linha in transposta:
        print(linha)

def imprimirdiagonais(matriz):
    diagonalprincipal = [matriz[i][i] for i in range(len(matriz))]
    diagonalsecundaria = [matriz[i][len(matriz)-1-i] for i in range(len(matriz))]
    print("Diagonal principal:", diagonalprincipal)
    print("Diagonal secundária:", diagonalsecundaria)

def main():
    matriz = []
    valor = 0

    def valoresmaioresque(matriz, valor):
        contador = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] > valor:
                    contador += 1
        return contador

    opcoes = {
        1: lambda: preencher_matriz(int(input("Digite o número de linhas: ")), int(input("Digite o número de colunas: "))),
        2: lambda: imprimir_matriz(matriz),
        3: lambda: somadiagonalprincipal(matriz),
        4: lambda: transposta(matriz),
        5: lambda: print("Quantidade de valores maiores que:", valor, "é", valoresmaioresque(matriz, valor)),
        6: lambda: imprimirdiagonais(matriz),
        7: lambda: exit(0)
    }

    while True:
        print("\nMenu:")
        print("1. Preencher matriz")
        print("2. Imprimir matriz")
        print("3. Somar Diagonal Principal")
        print("4. Matriz Transposta")
        print("5. Valores maiores que o Elemento")
        print("6. Imprimir Diagonal Principal e Secundaria")
        print("7. Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha in opcoes:
            if escolha == 1:
                matriz = opcoes[escolha]()
            elif escolha == 5:
                valor = int(input("Digite um valor: "))
                opcoes[escolha]()
            else:
                opcoes[escolha]()
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
