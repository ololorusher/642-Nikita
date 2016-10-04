__author__ = 'student'

a = input().split()
t=int(input())
q=len(a)
for i in range(t):
    b=int(a[q-1])
    a.insert(q-1-b, a[q-1])
print(a[0:q])