# count recursively
def count(n, i=1):
    print(i)
    if i > n:
        return 
    return count(n, i+1)

count(10)
     
