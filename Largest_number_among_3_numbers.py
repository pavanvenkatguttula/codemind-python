a,b,c=map(int,input().split())
if a>b and a>c:
    d=a
elif b>a and b>c:
    d=b
else:
    d=c
print(d)