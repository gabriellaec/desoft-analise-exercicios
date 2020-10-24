mes_letra = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
mes_numero = [1,2,3,4,5,6,7,8,9,10,11,12]
i=0
while i < len(mes_letra):
    x = str(input("Digite o nome de um mês: "))
    if x == mes_letra[i]:
        print(mes_numero[i])
    i+=1    
    