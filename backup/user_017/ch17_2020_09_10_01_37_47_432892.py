def eh_bissexto(x):
    if 4*x:
        return "True"
    elif 10*x:
        return "False"
    else:
        return "False"
x=2020
a= eh_bissexto(x)
print(a)
