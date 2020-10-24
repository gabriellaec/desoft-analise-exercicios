from random import randint
dinheiros==1000
while (dinheiros>0):
    apostar=input("Apostar?")
    if apostar=="não":
        print("Você terminou a partida com {0} dinheiros".format(dinheiros))
        break
    else:
        primeiro_dado=randint(1,6)
        segundo_dado=randint(1,6)
        soma_dados=primeiro_dado + segundo_dado
        chute1=int(input("Chute um número:"))
        dinheiros-=30
        if chute1==soma_dados:
            dinheiros+=50
            print("Você terminou a partida com {0} dinheiros".format(dinheiros))
        else:
            cont_des=input("Continuar tentando ou desistir?")
            if cont_des=="desistir":
                print("Você terminou a partida com {0} dinheiros".format(dinheiros))
                continue
            else:
                chute2=int(input("Chute outro número:"))
                dinheiros-=20
                if chute2==soma_dados:
                    dinheiros+=50
                    print("Você terminou a partida com {0} dinheiros".format(dinheiros))
                else:
                    print("Valor de um dos dados:{0}".format(primeiro_dado))
                    cont_desi=input("Continuar tentando ou desistir?")
                    if cont_desi=="desistir":
                        print("Você terminou a partida com {0} dinheiros".format(dinheiros))
                        continue
                    elif cont_desi=="continuar":
                        chute3=int(input("Chute outro número:"))
                        dinheiro-=10
                        if chute3==soma_dados:
                            dinheiro+=50
                            print("Você terminou a partida com {0} dinheiros".format(dinheiros))
                            continue
                                 
                           
                     
                  
    