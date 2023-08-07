import random
import string

from palavras import palavras_forca
from visualdaforca import visualdasvidas

def palavravalida(palavras_forca):
    palavra = random.choice(palavras_forca)

    while '-' or ' ' in palavras_forca:
        palavra = random.choice(palavras_forca)

    return palavra.upper()    

def forca():
    palavra = palavravalida(palavras_forca)
    letraspalavra = set(palavra) #Letras das Palavras
    alfabeto = set(string.ascii_uppercase)
    letrasusadas = set() #Rastrear as letras já usadas pelo usuário

    vidas = 5

    #O que a palavra que está sendo adivinhada pelo usuário atualmente é
    listadaspalavrasusadas = [letra if letra in letrasusadas else '-' for letra in palavra]
    print('Palavra: ', ' '.join(listadaspalavrasusadas))

    while len(letraspalavra) > 0 and vidas > 0:
        print(visualdasvidas[vidas])
        print('Você tem', vidas, 'vidas restantes e já usou estas letras:', ' '.join(letrasusadas))
        entradausuario = input('Entre com um caractére').upper()

        if entradausuario in alfabeto - letrasusadas:
            letrasusadas.add(entradausuario)
            if entradausuario in letraspalavra:
                letraspalavra.remove(entradausuario)
            else:
                vidas -= 1 #Tira uma vida se a letra não estiver na palavra

        elif entradausuario in letrasusadas:
            print('Você já usou essa letra')

        else:
            print('Caractére inválido. Por favor, entre com um válido.')

    if vidas == 0:
        print(visualdasvidas[vidas])
        print('Você morreu. A palavra era',palavra)
    else:
        print('Você adivinhou a palavra e salvou a pessoa!')

if __name__ == '__main__':
    forca()        

        


    
    
