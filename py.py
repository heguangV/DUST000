def happy(x):
    a=0
    for i in str(x):
        a+=int(i)**2
    if a==1:
        return 1
    else:
        return a

x=int(input())
t=1  #t用来计数
while happy(x)!=1:
    x=happy(x)
    t+=1
    if t>50:
        print("False")
        exit()
print("True")