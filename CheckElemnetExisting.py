n = int(input("Enter the size of a list: "))
print("Enter the elements of the list: ")
List = []
for i in range(n):
    element = (input())
    List.append(element)
print("Enter the element you want to search: ")
element = input()
if element in List:
    print("The element is present in the list")
else:
    print("The element is not present in the list")