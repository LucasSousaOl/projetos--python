from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('Jo')
sleep(1)
print("Ken")
sleep(1)
print('Pô!!')
print('-=' *15)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*15)
if computador == 0:
    if jogador == 0:
        print('Empatou !!')
    elif jogador == 1:
        print('Você ganhou!!')
    elif jogador == 2:
        print('Você perdeu!!')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('Você perdeu!!')
    elif jogador == 1:
        print('Empatou!!')
    elif jogador == 2:
        print('Você ganhou!!')
    else:
        print('Jpgada inválida!')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou!!')
    elif jogador == 1:
        print('Você perdeu!!')
    elif jogador == 2:
        print('Empatou!!')
    else:
        print('Jpgada inválida!')
else:
    print('Jogada inválida!')