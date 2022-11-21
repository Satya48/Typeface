def base3(N):
    if (N == 0):
        return
    x = N % 3
    N //= 3
    if (x < 0):
        N += 1
    base3(N)
    if (x < 0):
        print(x+(3* -1), end = "")
    else:
        print(x, end = "")
 
def convert(n): 
    if (n != 0):
        base3(n)
    else:
        print("0", end = "")
 
n=int(input())
convert(n)