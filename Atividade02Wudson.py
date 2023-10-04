#ATIVIDADE 02 - LUCAS MARTINS CIRILO - P1 - TARDE

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

#Resposta 4

nota1 = float(input("Digite a nota:"))
nota2 = float(input("Digite a nota:"))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")

#Resposta 5

valor1 = float(input("Digite o valor:"))
valor2 = float(input("Digite o valor:"))

if valor1 > valor2:
    maior = valor1
else:
    maior = valor2
    print(f"O Maior valor é: {maior}")

#Resposta 6

valor1 = float(input("Digite o valor:"))
valor2 = float(input("Digite o valor:"))

if valor1 < valor2:
    print(valor1, valor2)
else:
    print(valor2, valor1)

#Resposta 7

numero_da_conta = float(input("Digite o número da sua conta:"))
saldo = float(input("Digite o saldo da sua conta:"))
debito = float(input("Digite o débito da sua conta:")) 
credito = float(input("Digite o crédito da sua conta:"))

saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")

#Resposta 8

quantidade_atual = float(input("Digite a quantidade atual:"))
quantidade_maxima = float(input("Digite a quantidade máxima:"))
quantidade_minima = float(input("Digite a quantidade minima:"))

quantidade_media = (quantidade_minima + quantidade_maxima) / 2 

if quantidade_atual >= quantidade_media:
    print("Não efetuar compra")
else:
    print("Efetuar Compra")

#Resposta 9

nota01 = float(input("Digite a nota:"))
nota02 = float(input("Digite a nota:"))
media = (nota01 + nota02) / 2

if media >= 9.0 <= 10:
    notaconceito = "A"
elif media >= 7.5 < 9.0:
    notaconceito = "B"
elif media >= 6.0 < 7.5:
    notaconceito = "C"
elif media >= 4.0 < 6.0:
    notaconceito = "D"
else:
    notaconceito = "E"

print(nota01)
print(nota02)
print(media)
print(notaconceito)

if notaconceito == "A" or  notaconceito == "B" or notaconceito == "C":
    print("Aprovado! Tenha um FELIZ NATAL!! :D")
else:
    print("Reprovado! Sem natal para você :C")



# %%
