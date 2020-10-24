def PiWallis(n):
    produto=1
    i=1
    while i<=n:
        if i%2==0:
            a=i
            b=i+1
        else:
            a=i+1
            b=i
        produto=produto*(a/b)
        i=i+1
    final=produto*2
    return final
    