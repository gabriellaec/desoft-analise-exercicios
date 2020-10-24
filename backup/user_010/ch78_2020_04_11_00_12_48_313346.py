condição=True
atletas={}

while condição:
    nome=str(input("Qual o nome do corredor?"))
    if nome=="sair":
        condição=False
    else:
        aceleraçao=int(input("Qual a sua aceleração?"))
        atletas[nome]=aceleraçao

def calcula_tempo (lista):
    dic={}
    menortempo=1000000000000000000000
    for nome,aceleracao in lista.items():
        if aceleracao>0:
            tempo=((200)**(1/2))/(aceleracao**(1/2))
            dic[nome]=tempo
            if tempo<menortempo:
                menortempo=tempo
                ganhador=nome
            resultado=[menortempo,nome,dic]
        
    return resultado
resultado=calcula_tempo(atletas)
print ("O vencedor é {0} com tempo de conclusão de {1} s.".format(resultado[1],resultado[0]))