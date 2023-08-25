n=int(input())
a=n**2
y=(a-1)%9+1
if y==n:
    print("Neon Number")
else:
    print("Not Neon Number")