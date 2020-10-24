def verifica_progressao(lista):
    RazaoPA=n[i]-n[i+1]
    RazaoPG=n[i]/n[i+1]
    for i in range(lista):
        if RazaoPA==n[i+1]-n[i+2] and RazaoPG==n[i+1]/n[i+2]:
            return "AG"
        elif RazaoPA==n[i+1]-n[i+2]:
            return "PA"
        elif RazaoPG==n[i+1]/n[i+2]:
            return "PG"
        else:
            return "NA"
      

       
            
        