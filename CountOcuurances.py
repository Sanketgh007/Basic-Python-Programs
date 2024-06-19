n = int(input("Enter the size of a list: "))
print("Enter the elements of the list: ")
List = []
for i in range(n):
    element = input()
    List.append(element)

for i in List:
    count = 1
    for j in List:
        if i == j:
            count += 1
            List.remove(j)
    print("The number of times the element", i, "appears in the list is:", count)