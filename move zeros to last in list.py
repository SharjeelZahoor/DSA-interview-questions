# two sorted arrays sorted append in third array and it also should be sorted
lst = [0,3,4,0,0,0,4,9]
i = 0
for j in range(1, len(lst)-1):
    if lst[j] == 0:
        j+=1
    if lst[i] == 0:
        if lst[j]>0:
            lst[i], lst[j] = lst[j], lst[i]
            j+=1
            i+=1
    if lst[i] != 0:
        i+=1
print(lst)
