# fizzbuzz

def fizzbuzz(n):
    for i in range(1,n+1):
        if i%15 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 ==0 :
            print("Buzz")
        else:
            print(i)


fizzbuzz(20)


for i in range(1,11):
    print(i)
