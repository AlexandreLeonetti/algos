# given a sorted array, remove duplicates in place




def rm_duplicates(arr):
    if not arr:#edge case empty list
        return 0

    i=0 # pointer for unique elements

    for j in range(1,len(arr)-1):# start j from 1 to compare with i
        if arr[i]!=arr[j]: # if j different from i (0 diff 1), then increase i of one to avoid missing unique value of i
            i = i+1 #increase unique pointer to j
            arr[i]=arr[j]# overwrite next unique pos with unique val 
    return i+1 


a = [2,3,3,3,3,3,3,5,6,7,7,7]
print(a)
b = rm_duplicates(a)
print(a[:b])

          