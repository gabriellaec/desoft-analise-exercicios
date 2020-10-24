def PiWallis(n):
    a=0
    b=0
    produto=1
    i=1
    while i<=n:
        if n%2==0:
            a=n
            b=n+1
        else:
            a=n+1
            b=n
        produto=produto*(a/b)
        n=n+1
    final=produto*2
    return final
    