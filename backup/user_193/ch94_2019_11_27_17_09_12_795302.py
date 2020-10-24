vmaxkm=int(input("Qual a velocidade máxima da via (em km/h)? "))
vmax=vmaxkm/3.6
dis=int(input("Qual a distância entre as câmeras (em metros)? "))
vazio=[""," "]
placa="dro0818"
placas=[]
insts=[]
caracpermitidas=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","1","2","3","4","5","6","7","8","9","0"]
while placa not in vazio:
    placa=input("Digite a placa: ")
    if len(placa)>7 or len(placa)<7:
        print("Uma placa tem 7 caracteres!")
        continue
    placam=placa.lower()
    placas.append(placam)
    i=0
    while i<len(placa):
        if placam[i] not in caracpermitidas:
            continue
            saida="1"
        i+=1
    if saida=="1":
        continue
    instante=int(input("Digite o instante (em segundos): "))
    insts.append(instante)
    c=0
    while c<len(placas)-1:
        if placas[c]==placas[c+1]: #arrumar
            if (dis/(insts[c+1]-insts[c]))>vmax:
                if (dis/(insts[c+1]-insts[c]))<=(1.2*vmax):
                    print("Infração média! Você foi multado em R$130,16")
                elif (dis/(insts[c+1]-insts[c]))<=(1.5*vmax):
                    print("Infração grave! Você foi multado em R$195,23")
                elif (dis/(insts[c+1]-insts[c]))>(1.5*vmax):
                    print("Infração gravíssima! Você foi multado em R$585,69; sua CNH foi suspensa e será apreendida.‬")
        c+=1