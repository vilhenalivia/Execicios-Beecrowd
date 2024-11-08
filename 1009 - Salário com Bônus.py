from decimal import Decimal

nome_vendedor = input('Primeiro nome do vendedor: ')
salario_fixo =  Decimal(input('Salário fixo:'))
total_vendas = Decimal(input('Total a receber no final do mês:'))

total = ((total_vendas / 100) * 15 ) + salario_fixo

print(F'TOTAL = R$ {total:.2f}')