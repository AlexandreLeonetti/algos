# fibonacci algo

arr = {} 

def fibonacci(n):
    if n == 0:
        return 1
    elif n==1:
        return 1
    else:
        if n in arr.keys():
            return arr[n]
        else:
            arr[n]= fibonacci(n-1)+fibonacci(n-2)
        return arr[n] 


print(fibonacci(100))
