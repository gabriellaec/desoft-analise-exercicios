with open ('macacos-me-mordam.txt','r') as arquivo:
    conteudo=arquivo.read()
    palavras=conteudo.split()
    correcao=[]
    for palavra in palavras:
        correcao.append (palavra.lower())
n=0
for palavra in correcao:
    if palavra=='banana':
        n+=1