def object(s):
    #start
    m = 0
    #end
    n = len(s)-1
    while m < n:
        if s[m] != s[n]:
            return False
        m=m+2
        n=n-1
    return True

t = int(input())
for m in range(t):
    s = str(input())
    print(object(s))


