vsh = {'enrico' : '04/04/2001', 'lucas' : '23/12/2001', 'tonto': '06/09/2001'}        
def aniversariantes_de_setembro(vsh):
    novod = {}
    for nome,setembro in vsh.items():
        if setembro[4] == '9':
            novod[nome]= setembro
    return novod
print(aniversariantes_de_setembro(vsh))
        