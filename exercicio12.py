from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

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
print('-=' * 15)

# Validação antes de mostrar a jogada do jogador
if jogador < 0 or jogador > 2:
    print('Jogada inválida!')
else:
    print(f'O computador jogou {itens[computador]}')
    print(f'O jogador jogou {itens[jogador]}')
    print('-=' * 15)

    if computador == 0:  # Pedra
        if jogador == 0:
            print('Empatou!!')
        elif jogador == 1:
            print('Você ganhou!!')
        elif jogador == 2:
            print('Você perdeu!!')

    elif computador == 1:  # Papel
        if jogador == 0:
            print('Você perdeu!!')
        elif jogador == 1:
            print('Empatou!!')
        elif jogador == 2:
            print('Você ganhou!!')

    elif computador == 2:  # Tesoura
        if jogador == 0:
            print('Você ganhou!!')
        elif jogador == 1:
            print('Você perdeu!!')
        elif jogador == 2:
            print('Empatou!!')
