a=[]
for i in range(1,51):
    a.append(i)
print(a)
a.sort(reverse=True)
smax=0
for x in range(0,48):
    if a[x]+a[x+1] > a[x+2] and a[x]< a[x+1]+a[x+2] and -a[x]+a[x+1] < a[x+2]:
        q=(a[x]+a[x+1]+a[x+2])/2
        s=(q*(q-a[x])*(q-a[x+1])*(q-a[x+2]))**0.5
    if s > smax:
        smax=s
        b1=a[x]
        b2=a[x+1]
        b3=a[x+2]
    break
if smax==0:
    print("Er")
else:
    print(smax)
    print(b1,b2,b3)
