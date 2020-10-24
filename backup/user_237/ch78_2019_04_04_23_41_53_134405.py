programa = True
atletas = {}
while programa == True:
    nome = input("Qual é o nome?:")
    if nome == "sair":
        programa = False
    else:
    	aceleracao = float(input("Aceleracao?:"))
		atletas[nome] = aceleracao

def vencedor(t1):
    lista_tempos = t1.values()
                           



def calcula_tempo(atletas):
    tempos = {}
    for k,v in atletas.items():
        tempos[k] = (200/v)**(0.5)
    return tempos