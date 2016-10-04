__author__ = 'student'
k=int(input())
n=int(input())
a=[]
for i in range (n+2):
    x=0
    if i<k:
        a.append(1)
    else:
        for j in range (k):
            x+=a[i-1-j]
        a.append(x)
print(a[n])