def verifica_progressao(n):
    for i in len(n+1):
        if n[i]-n[i+1]==n[i+1]-n[i+2] and n[i]/n[i+1]==n[i+1]/n[i+2]:
            return "AG"
        elif n[i]-n[i+1]==n[i+1]-n[i+2]:
            return "PA"
        elif n[i]/n[i+1]==n[i+1]/n[i+2]:
            return "PG"
        else:
            return "NA"
      

       
            
        