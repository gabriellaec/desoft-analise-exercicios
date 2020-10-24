d=input('nome do mes?')
lista=['nao existe',"janeiro",'fevereiro','março',"abril",'maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
for n in range(len(lista)):
    if lista[n]==d:
        print(n)

dic={'janeiro':1, 'fevereiro':2,'março':3,"abril":4,'maio':5,'junho':6,'julho':7,'agosto':8,'setembro':9,'outubro':10,'novembro':11,'dezembro':12}
numero=dic[d]