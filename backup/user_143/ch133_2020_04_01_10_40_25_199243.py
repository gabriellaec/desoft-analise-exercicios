perg=input('Está funcionando?')
while perg!=n or perg!=s:
    perg=input('Está funcionando?')
if perg==s:
    print('Sem problemas!')
else:
    p=input('Você sabe corrigir?')
    while p!=n or p!=s:
        p=input('Você sabe corrigir?')
    if p==s:
        print('Sem problemas!')
    else:
        pe=input('Você precisa corrigir?')
        while pe!=n or pe!=s:
            pe=input('Você precisa corrigir?')
        if pe==n:
            print('Sem problemas!')
        else:
            print('Apague tudo e tente novamente')
        