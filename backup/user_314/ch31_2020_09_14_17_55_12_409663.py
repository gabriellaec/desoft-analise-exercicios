def eh_primo(n):
    i=1
    contador=0

    while(n>=i):
        if(n%i==0):
          contador+=1;
        i+=1

    if(contador!=2):
      return False
    else:
      return True