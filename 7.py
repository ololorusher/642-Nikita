__author__ = 'student'
import math
A=list(map(int, input().split()))
c=0
n=0
for i in range (len(A)):
    if A[i]==2:
        if i==len(A)-1:
            c+=A[i]
            n=n+1
            break
        else:
            if A[i+1]==2:
              c+=A[i]
              n=n+1
    else :
        c+=A[i]
        n=n+1
print(c//n)