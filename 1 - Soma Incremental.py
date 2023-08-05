def main():
    soma = 0

    while True:
        opcao_continua = input("Digite um número para somar ou 'nao' para sair: ")

        if opcao_continua.lower() == 'nao':
            break

        try:
            valor_soma = int(opcao_continua)
            soma += valor_soma
            print(f"A soma é: {soma}")
        except ValueError:
            print("Valor inválido! Tente novamente.")

    print("Programa encerrado.")


if __name__ == "__main__":
    main()
