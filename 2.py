__author__ = 'student'

A = [1, 2, 3, 4, 5]

for i in range(0, len(A)-1, 2):
    A[i], A[i+1] = A[i+1], A[i]
print (A)



B = [1, 2, 3, 4, 5]

B.insert(0, 5)
print(B[0:len(B)-1:1])



C = [1, 2, 2, 3, 3, 3]
for i in range (0, len(C), 1):
    c = C.count(C[i])
    if c == 1:
        print (c)

k = 0
D = [1, 2, 3, 4, 5, 6]
d = D.count(D[0])
for i in range (0, len(D), 1):
    if D.count(D[i]) > d:
        d = D.count(D[i])
        k = i

print (D[k])