Programa_Rodando = True
lista = []

while Programa_Rodando:
  palavra = input("Digite a Palavra:")
  if palavra == 'fim':
    Programa_Rodando = False
    for n in range(0,len(lista)):
      print(lista[n])
  else:
    if palavra[0] == 'a':
      lista.append(palavra)