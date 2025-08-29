def main():
    for a in range (1,6,2):
        sum=0
        m=a
        while(sum+m<765):
            sum+=m
            m*=2
        if sum+m == 765:
            break
    for x in range(0,8):
        print(a)
        a*=2
if __name__ == "__main__":
    main()

