## Calculo de salário 

import locale

locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')

#nome = input("Qual é o seu nome ? ")
salario = float(input("Qual é o seu salario ?"))

new_salario = locale.atof(salario)

horasTrabalhadas = float(input("Quantas horas trabalhas na semana ?"))

#print(f"Seu nome é: {nome}")
##print(f"Seu salário:{3000}")

valorDia = salario/horasTrabalhadas

#round (valorDia, 2)

print(f"Sua diaria vale: {valorDia: .2f}")
print ("-------------------------------")
horasDia = float(input("quantas horas voce trabalha por dia ?"))
print (f'Sua hora é: {valorDia / horasDia: .2f}')