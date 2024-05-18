# cook your dish here
t=int(input())
for i in range(t):
    cnt=0
    a=input().split()    #['4','4']
    n=int(a[0])
    k=int(a[1])
    s=input().split()  #['2','1','6','7']
    sum=0
    for i in range(len(s)):
        sum+=int(s[i])
    for j in range(len(s)):
        if int(s[j])+k > sum-int(s[j]) :
            cnt+=1
        else:
            cnt+=0
    print(cnt)