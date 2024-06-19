num = int(input("Enter a number: "))
#def factorial(num):
    #if num == 0:
       # return 1
    #else:
       # return num * factorial(num-1)
#print("The factorial of", num, "is", factorial(num)) 
#Approach 2
if num<0:
    print("It is invalid input")
elif num==0:
    print("The factorial of 0 is 1")
else:
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print("The factorial of", num, "is", fact)