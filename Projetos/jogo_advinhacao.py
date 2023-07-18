                 
## Jogo de advinhação ##

import random

numero = random.randint(1,100)
tentativa = 0
numero_jogadas = 1
LIMITE_JOGADAS = 4

while numero_jogadas <= LIMITE_JOGADAS :
    
    tentativa = int(input("Faça a sua jogada, esolha um numero de 1 a 100: "))

    if numero_jogadas >= LIMITE_JOGADAS:
        print("Você perdeu!! O numero correto era", numero)
        break
    elif tentativa == numero:
        print("Parabens!! Você advinhou o numero em ",numero_jogadas, "tentativas." "O número correto era" , numero)

    elif tentativa < numero:
        print("O numero é maior que ", tentativa)
        numero_jogadas += 1

    elif tentativa > numero:
        print("O numero é menor que", tentativa)
        numero_jogadas += 1

    