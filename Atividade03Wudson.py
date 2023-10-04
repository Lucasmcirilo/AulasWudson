#ATIVIDADE 03 - LUCAS MARTINS CIRILO - P1 - TARDE

#Resposta 01

for numero in range(1000, 2001):
    if numero % 11 == 5:
        print(numero)

#Resposta 02

for numero in range(1, 11):
    print(f"tabuada do {numero}")
    for tabuada in range(1, 11):
        resultado = numero * tabuada
        print(f"{numero} * {tabuada} = {resultado}")                   

#Resposta 03

lista_de_amigos = ['Rodrigo', 'Micael', 'Matheus', 'Gleyson']
for amigos in range(0, 4):
    print(f'Amigo:{lista_de_amigos[amigos]}')

#Resposta 04

tabuadanum = int(input("Digite o numero desejado:"))

for tamanhotabuada in range(0, 11):
    res = tabuadanum * tamanhotabuada
    print(res)

#Resposta 05

lista_de_amigos = ['Rodrigo', 'Micael', 'Matheus', 'Gleyson']
for amigos in range(0, 4):
    print(f'Eae {lista_de_amigos[amigos]} como que você ta?')

#Resposta 06

#Não consegui fazer :c


    