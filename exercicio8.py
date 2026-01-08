peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura **2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif 18.5 <= imc <= 25:
    print('Você está no peso ideal!')
elif 25 < imc <= 30:
    print('Você está no sobrepeso!')
elif 30 < imc <=40:
    print('Você está na obesidade!')
elif imc > 40:
    print('Você está na obesidade mórbida, CUIDADO!!')
