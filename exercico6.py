from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <=9:
    print('A categoria do atleta é mirim.')
elif idade > 9 and idade <= 14:
    print('A categoria do atleta é infantil')
elif idade > 14 and idade <= 19:
    print('A categoria do atleta é junior')
elif idade >19 and idade <=25:
    print('A categoria do atleta é sênior')
elif idade >25:
    print('A categoria do atleta é master')