from datetime import datetime
def main():
    a,b=input().split(",")
    fmt = "%Y-%m-%d %H:%M:%S"
    c = datetime.strptime(a, fmt)
    d = datetime.strptime(b, fmt)
    e= abs((c - d).total_seconds())
    e = int(e // 60)
    print(abs(e))

if __name__ == "__main__":
    main()