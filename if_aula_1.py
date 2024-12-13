valor1=10
valor2=10
if valor2>valor1:
    print("valor 2 e maior")
elif valor1==valor2:
    print("sao iguais")

else :
    print("valor 1 e maior")


    
qtfalta= int(input("numero de faltas:"))
mediaf =float(input("media final:"))

if qtfalta<=5 and mediaf>=7 :
    print("aprovado")

else:
    print("reprovado")


numero=1
while numero !=0:
    numero =int (input("digite um numero: "))
    if numero % 2== 0:
        print("par")
    else:print("impar")
