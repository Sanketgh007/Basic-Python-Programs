import re
str = input("Enter a string ")
url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
if url:
    print("URL found", url)
else:
    print("URL not found")