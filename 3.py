__author__ = 'student'

A = input().split()
if len(A)%2 ==0:
    for i in range(0, (len(A)//2)):
        print(A[i], A[len(A)-i-1], end=' ')
else:
    for i in range (0, (len(A)//2)+1):
        if A[i]==A[len(A)-i-1]:
            print (A[i], end=' ')
        else:
            print(A[i], A[len(A)-i-1], end=' ')