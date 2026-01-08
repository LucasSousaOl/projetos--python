tot18 = masc = fem20 = 0
while True:
    print('-_'*20)
    idade = int(input('Idade: '))
    if idade >= 18:
        tot18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        masc +=1
    if sexo == 'F' and idade <20:
        fem20 +=1
    resp =' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {masc} homens cadastrados.')
print(f'E temos {fem20} mulheres com menos de 20 anos')
