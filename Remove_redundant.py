n = int(input("How many words do you want to enter? "))
unique_words = []

for i in range(n):
    word = str(input())
    if word not in unique_words:
        unique_words.append(word)

print("The unique words are: ")
print(unique_words)