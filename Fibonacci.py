num = int(input("Enter a number: "))
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
print("Fibonacci value of entered number is ",fibonacci(num))        