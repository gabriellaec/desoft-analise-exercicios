with open("churras.txt") as arquivo:
    produtos=[]
    quantidade=[]
    preco=[]
    for line in arquivo:
        string=str(line)
        produtos.append(string[::","])
        quantidade.append(int(string[","::","]))
        preco.append(int(string[","::]))
    valor_final=[]
    for qtdd,prc in quantidade, preco:
        valor_final.append(qtdd*prc)
        
    print(sum(valor_final))