with open("churras.txt") as arquivo:
    quantidade=[]
    preco=[]
    for line in arquivo:
        string=str(line)
        posicao_virg1=string.find(",")
        x=string[posicao_virg1:]
        posicao_virg2=x.find(",")
        quantidade.append(x[:posicao_virg2])
        preco.append(x[posicao_virg2:])
    valor_final=[]
    for qtdd,prc in quantidade, preco:
        valor_final.append(qtdd*prc)
        
    print(sum(valor_final))