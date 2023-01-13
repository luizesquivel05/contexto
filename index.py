import os
import random
import time

# listas de palavras possíveis.
palavras = [['abacate', 'abacaxi', 'amendoim', 'alface', 'ameixa', 'amanhã'], ['bobo', 'beco', 'beijo', 'biscoito', 'bolacha', 'boicote'], ['casca', 'casa', 'caixa', 'cascudo', 'celular', 'computador']]

# processo para pensar uma palavra.
letra = int(random.uniform(0, 2))
palavra = int(random.uniform(0, 6))

print("PENSANDO NA PALAVRA!")
print("POR FAVOR AGUARDE")

time.sleep(4)
# processo para limpar tela.
try:
    os.system('cls')
except:
    os.system('clear')
    
print("PENSAMOS NA PALAVRA!")
time.sleep(2)

while True:
    # processo para limpar tela.
    try:
        os.system('cls')
    except:
        os.system('clear')

    tentativa = str(input('Faça tentativa da palavra: '))
    pensada = palavras[letra][palavra]
    pensada = str(pensada)
    # verificar se acertou.
    if pensada == tentativa:
        print("Parabéns, belíssima tentativa!")
        print("Você acertou!!")
        break
    else:
        # verificar o quanto você errou.
        if tentativa in palavras: print("SUA TAXA DE ACERTO FICOU EM 50%")
        elif tentativa in palavras[letra]: print("SUA TAXA DE ACERTO FICOU EM 80%")
        else: print("SUA TAXA DE ACERTO FICOU EM 30%")
        print("Hahaha, boa tentativa, infelizmente, você errou.")
        # verificar se quer continuar.
        print("\n\nDigite 0 para TENTAR NOVAMENTE e 1 para TERMINAR PROGRAMA.")
        if int(input()) == 1: break