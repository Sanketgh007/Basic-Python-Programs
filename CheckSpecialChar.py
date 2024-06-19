import re
str = input("Enter a string ")
regex = re.compile('[!@#$%^&*()_+}{":?><]')
if regex.search(str):
    print("Special characters found")
else:
    print("Special characters not found")