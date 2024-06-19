num = int(input("Enter a size of an array: "))
print("Enter the elements of the array: ")
Array = []
for i in range(num):
    element = int(input())
    Array.append(element)
    Array.sort()
print("The smallest element of the array is: ", Array[0])
print("The largest element of the array is: ", Array[num-1])