vmaxkm=int(input("Qual a velocidade máxima da via (em km/h)? "))
vmax=vmaxkm/3.6
dis=int(input("Qual a distância entre as câmeras (em metros)? "))
vazio=[""," "]
placa="dro0818"
placas=[]
insts=[]
saida=0
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
            saida=True
        i+=1
    if saida is True:
        continue
    instante=int(input("Digite o instante (em segundos): "))
    insts.append(instante)
    c=0
    while c<len(placas)-1:
        ind=1
        while ind<len(placas)-1:
            if placas[c]==placas[c+ind]:
                if (dis/(insts[c+ind]-insts[c]))>vmax:
                    if (dis/(insts[c+ind]-insts[c]))<=(1.2*vmax):
                        print("Infração média! Você foi multado em R$130,16")
                    elif (dis/(insts[c+ind]-insts[c]))<=(1.5*vmax):
                        print("Infração grave! Você foi multado em R$195,23")
                    elif (dis/(insts[c+ind]-insts[c]))>(1.5*vmax):
                        print("Infração gravíssima! Você foi multado em R$585,69; sua CNH foi suspensa e será apreendida.‬")
            ind+=1
        c+=1