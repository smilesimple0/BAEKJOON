a, b, c = map(int,input().split())

if a == b:
    if a == c:
        print(10000+a*1000)
    else:
        print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    x = [a,b,c]
    max(x)
    print(max(x)*100)