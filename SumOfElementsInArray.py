#import numpy as np
#Array = list(map(int, input("Enter the elements of the array: ").split()))
#print("The sum of the elements of the array is: ", np.sum(Array))
#Approach2
Array=[]
num = int(input("Enter size of array: "))
print("Enter the elements of the array: ")
for i in range(num):
    element = int(input())
    Array.append(element)
print("The sum of the elements of the array is: ", sum(Array))