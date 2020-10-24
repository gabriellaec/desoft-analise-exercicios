def subtracao_de_listas(l,s):
    l = [10,7654,32,7]
    s = [7654,10,32,3.1]
    ans = [l[i]-s[i] for i in xrange(min(len(l), len(s)))] 
    print (ans) 
        
    
