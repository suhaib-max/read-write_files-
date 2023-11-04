# # there is a method called open ( inbuilt method )
# file = open("new_file.txt")
# # read method return content of the file as a string
# contents = file.read()
# print(contents)
# # we have to close the file, it takes up some resources of computer
# file.close()

### it hard to remember close the file

# with keyword
with open("new_file.txt") as file:
    contents = file.read()
    print(contents)



