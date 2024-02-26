n=int(input())
p=list(map(int,input().split()))
res={}
for i in p:
    if i in res:
        res[i] +=1
    else:
        res[i]=1
for i,count in res.items():
    if count!=2:
        print(i)
