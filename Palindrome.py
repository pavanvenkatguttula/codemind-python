n=int(input())
p=0
q=n
while q!=0:
    r=q%10
    p=p*10+r
    q=q//10
if p==n:
    print("Palindrome")
else:
    print("Not Palindrome")