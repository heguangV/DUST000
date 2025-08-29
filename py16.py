def wall(a):
    big=1
    small=1
    b=0
    s=0
    day=0
    while(b+s<a):
        day=day+1
        if(b+s+big+small>=a):
            r=a-b-s
            b=b+r/(big+small)*big
            s=s+r/(big+small)*small
            break
        else:
            b=b+big
            s=s+small
            big*=2
            small*=0.5
    return day,b,s


def main():
    a=input()
    print(wall(int(a))[0])
    if wall(int(a))[1] == 1:
        print("1 1")
        return
    b= round(wall(int(a))[1],1)
    c= round(wall(int(a))[2],1)
    print(f"{c} {b}")

if __name__ == "__main__":
    main()