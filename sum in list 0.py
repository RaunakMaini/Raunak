a=[10,-10,20,30,-30,40,50,-50]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(i+2, len(a)):
            for l in range(i+3, len(a)):
                if a[i]+a[j]+a[k]+a[l]==0:
                    print(a[i],a[j],a[k],a[l])
            if a[i] + a[j] + a[k] ==0:
                print(a[i],a[j],a[k])
        if a[i] + a[j]==0:
            print(a[i],a[j])
    
