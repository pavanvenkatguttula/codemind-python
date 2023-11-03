r,c=map(int,input().split())
even=0
odd=0
for i in range(r):
    a=list(map(int,input().split()))
    if i%2==0:
        even=even+sum(a)
    else:
        odd=odd+sum(a)
print(even,odd)