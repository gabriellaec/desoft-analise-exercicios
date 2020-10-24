def verifica_progressao(num):
    i=0
    while i<(len(num)-2):
        if num[i+2]/num[i+1]==num[i+1]/num[i]:
            return "PG"
        elif num[i+2]-num[i+1]==num[i+1]-num[i]:
            return "PA"
        elif num[i+2]/num[i+1]==num[i+1]/num[i] and num[i+2]-num[i+1]==num[i+1]-num[i]:
            return "AG"
        else:
            return "NA"
        i=i+1