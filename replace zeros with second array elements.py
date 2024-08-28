# two sorted arrays sorted append in third array and it also should be sorted
lst1 = [1, 2, 3, 4, 0, 0, 0]
lst2 = [5, 6, 7]
i = 0
for j in range(len(lst1)):
    if lst1[j] == 0:
        lst1[j] = lst2[i]
        i+=1
print(lst1)

