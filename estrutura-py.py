texto = "aprendendo python na disciplina de linguagem de programação."

print(f"tamanho = {len(texto)}")
print(f"python in texto = {'python' in texto}")
print(f"quantidade de  y no texto = {texto.count('y')}")
print(f"as 5 primeiras letras são: {texto [0:6]}")

print(f"texto = {texto}")

print(f"tamanho do texto = {len(texto)}\n")
palavras = texto.split()
print(f"palavras = {palavras}")
print(f"tamanho das palavras = {len(palavras)}")
linguagens = ["Python", "Java","C"]
print( "antes da listcomp =", linguagens)
linguagens = [item.lower() for item in linguagens]
print("\ndepois da listcomp = ", linguagens)




vogais= ['a', 'e', 'i', 'o','u']#poderia ter usado aspas duplas

for vogal in vogais:
    print(f'Posição = {vogais.index(vogal)}, valor = {vogal}')