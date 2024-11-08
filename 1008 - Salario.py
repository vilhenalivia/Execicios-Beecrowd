from decimal import Decimal

numberFuncionario = int(input('Digite o número do funcionário: '))
horasTrabalhadas = int(input('Digite o números de horas trabalhadas: '))
valorHora = Decimal(input('Digite o valor a ser recebido por hora: '))

salario = horasTrabalhadas * valorHora

print(f'NUMBER = {numberFuncionario}')
print(f'SALARY = R$ {salario:.2f}')