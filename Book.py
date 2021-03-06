fp = open("book.txt", encoding="utf8")
# print(fp.read())
# we need to read the book, line by line

character = "Tom"
sum = 0
for line in fp:
    # I am on a single line inside the iteration
    sum = sum + (line.count(character))
print(f"the name {character} shows up {sum} times")
