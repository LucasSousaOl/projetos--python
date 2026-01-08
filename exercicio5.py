nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
soma = nt1 + nt2
resultado = soma /2
if resultado >=7:
    print('Tirando {} e {}, a média do aluno é {}'
          'O Aluno está aprovado'.format(nt1, nt2, resultado))
elif resultado <5:
    print('Tirando {} e {}, a média do aluno é {}'
          'O Aluno está reprovado.'.format(nt1, nt2, resultado))
else:
    print('Tirando {} e {}, a média do aluno é {}'
          'O aluno está de recuperação.'.format(nt1, nt2, resultado))
