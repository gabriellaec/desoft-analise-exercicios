aniversarios={'ana':{'dd':15,'mm':9,'aaaa':1999},'bia':{'dd':16,'mm':11,'aaaa':1998},'carlos':{'dd':28,'mm':9,'aaaa':1988}}
def aniversariantes_de_setembro(aniversarios):
    aniset={}
    for nome,aniversario in aniversarios.itens():
        if aniversarios[aniversario]['mm']==9:
            aniset[nome]=aniversario
    return aniset    
print(aniversariantes_de_setembro(aniversarios))
