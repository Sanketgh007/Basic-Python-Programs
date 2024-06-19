n = int(input("Enter the size of a list: "))
print("Enter the elements of the list: ")
List = []
for i in range(n):
    element = (input())
    List.append(element)
list2 = List[::-1]
print("The reversed list is: ", list2)