with open("churras.txt") as arquivo:
    quantidade=[]
    preco=[]
    for line in arquivo:
        string=str(line)
        posicao_virg1=string.find(",")
        x=string[(posicao_virg1+1):]
        posicao_virg2=x.find(",")
        quantidade.append(x[:posicao_virg2])
        preco.append(x[(posicao_virg2+1):])
    valor_final=[]
    i=0
    for qtdd in quantidade:
        valor_final.append(qtdd*preco[i])
        i+=1
        
    print(sum(valor_final))