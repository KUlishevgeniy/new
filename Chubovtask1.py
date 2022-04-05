b=list(input())
for i in range(0,len(b)):
    for k in range(i+1,len(b)):
        if b[k]<b[i]:
            s=b[k]
            p=b[i]
            b[k]=p
            b[i]=s

    print(b)