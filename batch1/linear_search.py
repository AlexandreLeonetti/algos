# returns first of occurrence of an element?

def search (arr, n):
    for i in range(len(arr)):
	    if arr[i] == n:
                return i

a = [5,8,9,3,4,2,5,6,9,0]

print(a)
print(search(a,0))
