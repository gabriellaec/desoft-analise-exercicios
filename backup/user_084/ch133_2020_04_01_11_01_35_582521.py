x=input('está funcionando?')
s='s'
n='n'
if x==s:
    print('sem problemas!')
elif x==n:
    y=input('você sabe corrigir? (n/s)')
    if y==s:
        print('sem problemas!')
    elif y==n:
        w=input('você precisa corrigir? (n/s)')
        if w==n:
            print('sem problemas!')
        elif w==s:
            print('apague tudo e temte novamente')
         

