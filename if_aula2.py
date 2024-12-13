numero=1
while numero !=0:
    numero = int(input("digite um numero: "))

    if numero % 2 == 0:
        print("nuemro par")
    else:
        print("numero impar")
        

nome = "guido"

for i, c in enumerate(nome):
    print(f"posicao ={i}, valor={c}")
