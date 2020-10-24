d=input('nome do mes?')
lista=['nao existe',"janeiro",'fevereiro','março',"abril",'maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
for n in range(len(lista)):
    if lista[n]==d:
        print(n)