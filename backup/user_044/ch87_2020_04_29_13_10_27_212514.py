with open('churras.txt', 'r') as arquivo:
    linhas=arquivo.readlines()
    custos=0
    for i in linhas:
        for x in i:
            if x==',': 
                s1=i.split(',')
                for n in s1:
                    if n==int:
                        for z in s1:
                            if z==float:
                                custos+=z*n
            else:
                s1=i.split()
                for n in s1:
                    if n==int:
                        for z in s1:
                            if z==float:
                                custos+=z*n
                
    print(custos)
                        
    