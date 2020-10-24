numero = int(input(“ate qual numero?”))
n = 2
while n <= numero:
    if n % 2 != 0:
        d = 3
        while d < n:
            if n % d == 0:
                print(“NAO É PRIMO”)
                x = False
        if x == True:
            print(“eh primo tiw”)