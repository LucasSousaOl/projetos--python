resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior= menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} númerios e sua média foi {}.'.format(quant, media))
print(' O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))
