def ls_digit(a):
    if a%3==2 and a%5==3 and a%7==2:
        return True
    else:
        return False


def main():
    k=0
    a=input()
    for i in range(1,int(a)+1):
        if ls_digit(i):
            print(i)
            k=k+1
    if k==0:
        print("No solution!")
if __name__ == "__main__":
    main()
