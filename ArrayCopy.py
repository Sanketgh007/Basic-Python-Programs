n = int(input("Enter the size of a list: "))
print("Enter the elements of the list: ")
List = []
List2=[]
for i in range(n):
    element = (input())
    List.append(element)
#List2 = List[:]
#List2.extend(List)
List2=list(List)
print("Copied list: ", List2)

