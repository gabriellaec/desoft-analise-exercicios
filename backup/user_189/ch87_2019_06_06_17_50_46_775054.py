with open('churras.txt','r') as churras:
    
    for a in churras.readlines():
        a.split(',')
        for b in a:
            if b == int or b == float:
                val=a[b]*a[b+1]
            	
         
                
        
	