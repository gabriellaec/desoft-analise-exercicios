def eh_bissexto(int(ano)):
    if ano%4==0 and ano%100!=0 :
        return "True"
    else:
        return "False"