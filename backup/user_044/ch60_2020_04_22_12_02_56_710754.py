def eh_palindromo(st1):
    st2=''
    x=len(st1)
    for i in range(len(st1)):
        st2.append(st1[x-i])
    if st1==st2:
        return True
    else:
        return False
    
        