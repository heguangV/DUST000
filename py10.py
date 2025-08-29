def main():
    a=input()
    b=a.split(" ")
    z=int(input())
    try:
        n = [int(num) for num in b]
    except ValueError:
        print("NO RESULT")
        return
    i = sorted(set(b))
    if 1<=z<=len(i):
        print(i[z-1])
    else:
         print("NO RESULT")

if __name__ == "__main__":
    main()