# rotate an array by k number
lst = [1,3,5,7,9]
k = 3
n = len(lst)
ans = [None]*n
for i in range(n):
    ans[ (i + k ) % n ] = lst[i]
    print(ans)