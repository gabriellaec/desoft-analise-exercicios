def collatz(primeiro_termo):
    while primeiro_termo<1000:
        if primeiro_termo%2==0:
            primeiro_termo=primeiro_termo/2
        else:
            primeiro_termo=(primeiro_termo*3)+1
        all_seq=[primeiro_termo]

        while primeiro_termo!=1:
            if primeiro_termo%2==0:
                x=primeiro_termo/2
                else:
                    y=(primeiro_termo*3)+1
                    all_seq.append(primeiro_termo)
                    a=len(max(all_seq))
                print(a)
    
    
    