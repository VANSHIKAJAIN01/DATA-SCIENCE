#factorial of a number:
f=1
n=int(input("ENTER A NUMBER : "))
for i in range(n,0,-1):
    f*=i
print("FACTORIAL : ",f)
