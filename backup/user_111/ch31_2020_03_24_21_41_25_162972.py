n=2
def eh_primo(numero):
    while n <= numero:
        if n%2 != 0:
            d=3
            while d<n:
                if n%d==0:
                    print("NAO É PRIMO")
                    x==False
                    d+=1
            if x==True:
                print("é primo")
            n+=1