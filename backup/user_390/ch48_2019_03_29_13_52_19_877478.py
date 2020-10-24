pergunta=input('fala um mes')
lista=[0,'Janeiro',"Fevereiro","Março",'Abril','Maio','Junho','Julho',"Agosto",'Setembro','Outubro','Novembro','Dezembro']
i=1
while i<len(lista):
    if lista[i]==pergunta:
        print (i)
    else:
        i+=1
