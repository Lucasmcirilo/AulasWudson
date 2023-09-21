#Resposta 1

numero = int(input("Digite um numero aqui:"))
if numero < 10: 
    print("Menor")
else:
    print("Maior")

#Resposta 2

numero = float(input("Digite um numero aqui:"))
if numero <= 0:
    print("Negativo")
else:
    print("Positivo")

#Resposta 3

numdemaca = int(input("Digite o numero de maçãs que deseja comprar:"))
if numdemaca < 12:
    custo = numdemaca * 1.30
else:
    custo = numdemaca * 1.00

print("O Custo da compra é",custo)

