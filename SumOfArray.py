n = int(input("Enter the size of a list: "))
print("Enter the elements of the list: ")
List = []
sum = 0
for i in range(n):
    element = int(input())
    List.append(element)
for i in List:
    sum = sum + i
print("The sum of the elements in the list is:", sum)