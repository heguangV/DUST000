def f(chars):
    #设计函数体，完成题目功能要求
    a={}
    c=""
    b=('0','1','2','3','4','5','6','7','8','9')
    for i in chars: 
        if i in (b):
            print('ERROR')
            exit()
        else:
            a[i]=a.get(i,0)+1
    for i in a:
        if a[i]==1:
            c=c+i
        else:
            c=c+i+str(a[i])
    return a,len(chars),c,len(c)   
n=input()
print(*f(n),sep='\n')