#fibonacci till n
n=int(input("ENTER THE LENGTH OF FIBONACCI : "))
a=0
b=1
if n==1 or n==0:
    print(0)
elif n==2:
    print(0,1,sep=" ")
else:
    print(0,1,sep=" ",end=" ")
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
