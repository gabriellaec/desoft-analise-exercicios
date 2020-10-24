palavra=input('Digite sua palavra para adicionar ou "fim" para imprimir as que começam em "a": ')
lista_final=[]
if palavra[0]=='a':
  lista_final.append(palavra)
while palavra!='fim':
  palavra=input('Digite sua palavra para adicionar ou "fim" para imprimir as que começam em "a": ')
  if palavra[0]=='a':
    lista_final.append(palavra)
print(lista_final)