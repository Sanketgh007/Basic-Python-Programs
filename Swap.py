num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
#Approach1
#temp = num1
#num1 = num2
#num2 = temp\
#Approach2
#num1, num2 = num2, num1
#Approach3
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("The numbers after swapping are", num1, num2)
