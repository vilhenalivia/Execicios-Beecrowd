from _decimal import Decimal

notaA = float(input('Digite a primeira nota: ')) 
notaB = float(input('Digite a segunda nota: '))

media = Decimal(((notaA * 3.5) + (notaB *7.5))/11)

print(f"Média = {media: .5f}"); 