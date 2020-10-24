with open('churras.txt', 'r') as arquivo:
    ler=arquivo.read()
    p=ler.split("\n")
lista=[]
resultado=0
for ele in p:
    lista.append(ele.split(","))
for listainfo in lista:
    valor_do_produto=float(listainfo[1])*float(listainfo[2])
    resultado+=valor_do_produto


print(resultado)