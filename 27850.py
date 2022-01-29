for i in range(245690,245756):
    k=0
    for j in range (1,i+1):
        if i%j==0: k=k+1
    if k==2: print(abs(245690-i)+1,i)