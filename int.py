## Calculo de salário 


#nome = input("Qual é o seu nome ? ")
salario = input("Qual é o seu salario ?")

salarioFormatado = "{:,.2f}".format(salario)
# Substitui o ponto decimal por vírgula para exibição brasileiras
salarioFormatadoVirgula = salarioFormatado.replace('.', ',')

# print(texto_formatado_com_virgula)
# Saída: 1.234,57


horasTrabalhadas = float(input("Quantas horas trabalhas na semana ?"))

#print(f"Seu nome é: {nome}")
##print(f"Seu salário:{3000}")

valorDia = salarioFormatadoVirgula/horasTrabalhadas

#round (valorDia, 2)

print(f"Sua diaria vale:")
print ("-------------------------------")
horasDia = float(input("quantas horas voce trabalha por dia ?"))
print (f'Sua hora é: {valorDia / horasDia: .2f}')