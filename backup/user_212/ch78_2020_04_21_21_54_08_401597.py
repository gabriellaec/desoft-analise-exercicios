dic_atletas={}
nome=str(input('Qual o nome do atleta ?')
a=float(input('Qual foi a aceleração do atleta?')
dic_atletas[nome]=a
                       
while nome != fim:
    dic_atletas[nome]=int(input('Qual foi a aceleração do atleta?')
    nome=str(input('Qual o nome do atleta ?')
    
def calcula_tempo (dic_atletas):
    dic_tempo={}
    for a in dic_atletas:
        dic_tempo[a]=(200/(dic_atletas[a]))**(1/2)
    return dic_tempo
             
maximok=max(dic_tempo, key=dic_tempo.get)
maximov=max(dic_tempo, value=dic_tempo.get)