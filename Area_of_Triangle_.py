a,b,h=map(int,input().split())
s=(b+h+a)/2
area= (s*(s-a)*(s-b)*(s-h)) ** 0.5
print(f"%.2f"%area)