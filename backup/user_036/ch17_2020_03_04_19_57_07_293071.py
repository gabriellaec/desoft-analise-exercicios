def eh_bissexto(x):
    if x%4==0:
        return 'True'
    if x%100!=0:
        return 'True'
    else:
        return 'False'
print(eh_bissexto(2000))