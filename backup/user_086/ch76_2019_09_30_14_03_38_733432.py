#dicionario[nomedapessoa]=dd/mm/aaaa
def aniversariantes_de_setembro(dicionario):
    setembro={}
    for i in dicionario:
         if dicionario[i][4]=='9':
            setembro[i]=dicionario[i]
    return setembro