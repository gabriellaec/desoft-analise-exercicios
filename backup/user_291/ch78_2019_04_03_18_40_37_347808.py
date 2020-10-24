atletas_dic = {}

atleta = input("Nome?" )

while atleta != "sair":
    
	aceleração = float(input("aceleração? "))
    
    atletas_dic[atleta] = aceleração
    
    atleta = input("Nome? ")

def calcula_tempo(atletas):
    
    tempo = {}
    
    for e in atletas:
        
        y = (200*atletas[e])**(1/2)
        
        tempo[e] = (y/atletas[e])
        
    return tempo

maior = 0

for e in tempo:
    
    if tempo[e] > maior:
        maior = tempo[e]
        vencedor = e

print("O vencedor é {0} com tempo de conclusão de {1} s".format(vencedor, maior))