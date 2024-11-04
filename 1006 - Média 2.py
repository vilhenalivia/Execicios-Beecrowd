from _decimal import Decimal

notaA = float(input('Digite a primeira nota: ')) 
notaB = float(input('Digite a segunda nota: '))
notaC = float(input('Digite a terceira nota: '))

media = Decimal(((notaA * 2) + (notaB * 3) + (notaC * 5))/10)

print(f"Média = {media:.1f}")