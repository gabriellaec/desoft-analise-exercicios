def eh_bissexto(x):
    if x%4==0:
        return 'true'
    if x%100!=0:
        return 'true'
    else:
        return 'false'
