with open("macacos-me-mordam.txt",'r') as file:
    arquivo = file.read()
arquivo2 = ''
for letra in arquivo:
    arquivo2 += letra.capitalize()
arquivo2 = arquivo2.split()
contador = 0
for palavra in arquivo2:
  if palavra == "BANANA":
      contador += 1
print(contador)