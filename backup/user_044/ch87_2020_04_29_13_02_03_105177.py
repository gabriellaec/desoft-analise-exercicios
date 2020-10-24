with open('churras.txt', 'r') as arquivo:
    linhas=arquivo.readlines()
    custos=0
    for i in linhas:
        s1=i.split(',')
        for i in s1:
            if i==int:
                for n in s1:
                    if n==float:
                        custos+=i*n
    print(custos)
                        
    