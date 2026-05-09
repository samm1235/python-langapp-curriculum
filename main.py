# file = open("words.txt", "r")
# line = file.readline()
# print(line)
# file.close()


# with open("words.txt", "r") as file:
#     line = file.readlines()
#     print(line)
#     for i in line:
#         print(repr(i))

file = open("words.txt", "w")
file.write("Hi")
file.write('Hello\n')
file.write("Whats up")