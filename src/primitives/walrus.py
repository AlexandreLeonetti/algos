user_input = input("Enter something (or 'q' to quit): ") # scanf once
print("some print once") # print once


while user_input != "q":
    print("while")
    print(f"You entered: {user_input}")
    user_input = input("Enter something (or 'q' to quit): ")  # Repeats input()

print("after while")



while (user_input := input("Enter something (or 'q' to quit): ")) != "q":
    print(f"You entered: {user_input}")


_test = "hello"

print(_test)

_test = 2
print(_test)


