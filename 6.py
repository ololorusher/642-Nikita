__author__ = 'student'
a=list(map(int, input().split()))
k=0
count1=0
count2=0
for i in range (len(a)):
    for j in range (len(a)):
         if a[j]>a[i]:
             count1+=1
         if a[j]<a[i]:
             count2+=1
    if count1==count2:
         print(a[i])
         break
    count1,count2=0,0