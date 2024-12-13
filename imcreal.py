peso =float (input("digite o peso em kg: "))
altura = float(input("digite a altura em metros: "))
imc=peso/(altura*2)
print(imc) 
if (imc<18.5): 
 
 print("abaixo do peso")
elif(imc<25):
 print("normal")
elif(imc<30):
 print("sobrepeso")
elif(imc<35):
 print("obesidade")