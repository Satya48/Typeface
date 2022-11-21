valid=['0','1','2','5','6','8','9']
n=int(input())
l=[]
x=1
y=1
while(y<=n):
    str1=str(x)
    c=0
    for i in str1:
        if(i in valid):
            c+=1
    if(c==len(str1)):
        l.append(str1)
        y+=1
    x+=1
f=l[len(l)-1]
f=int(f)
print(f)