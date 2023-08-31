n=int(input())
rev=0
q=n
while(q!=0):
   r=q%10
   rev=rev*10+r
   q=q//10
if rev==n:
     print("True")
else:
    print("False")
    