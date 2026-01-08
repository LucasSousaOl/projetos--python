from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0,10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer par ou ímpar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {pc}, o total foi {total}.')
    if tipo =='P':
        if total %2 ==0:
            print('Você venceu!')
            v +=1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v +=1
        else:
            print('Você perdeu!')
            break
    print('Vamos Jogar novamente...')
print(f'Game Over... Você venceu {v} vezes!')