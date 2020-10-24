def pos_arroba ("x"):
    i = 0
    a = "x"
    while i < len(a):
        if a[i] == "@":
            return a[i]
        else:
            i+=1
    