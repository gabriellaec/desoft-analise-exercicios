def PiWallis(n):
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
        i=i+1
    final=produto*2
    return final
    