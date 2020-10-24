lista_inversa=[]
teste_numero=int(input('Digite um número inteiro positivo para adicionar à lista e um número negativo ou zero para imprimir os número em ordem inversa: '))

while teste_numero>0:
  lista_inversa.insert(0, teste_numero)
  teste_numero=int(input('Digite um número inteiro positivo para adicionar à lista e um número negativo ou zero para imprimir os número em ordem inversa: '))

print(lista_inversa)