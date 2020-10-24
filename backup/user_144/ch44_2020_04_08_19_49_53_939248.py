
dic = {'JANEIRO': 1, 
       'FEVEREIRO': 2, 
       'MARÇO': 3,
       'ABRIL': 4,
       'MAIO': 5,
       'JUNHO': 6,
       'JULHO': 7,
       'AGOSTO': 8,
       'SETEMBRO': 9,
       'OUTUBRO': 10,
       'NOVEMBRO': 11,
       'DEZEMBRO': 12
       }

mes = input("Digite o mês: ")
for i in dic:
    if mes == i:
       
        print(f"{mes} é o mês de número {dic[i]}")