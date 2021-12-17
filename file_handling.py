# To create the file
# from os import write


# f = open("pk.txt","x")

# To write the file
# f = open("pk.txt","w")
# f.write("hi!!!\ni'm pk\ni'm learning python")
# f.close()

# f = open("pk.txt","r")
# print(f.read())

# f = open("pk.txt","r")
# print(f.readline())

# f = open("pk.txt","r")
# print(f.read(2))


f = open("pk.txt","a")
f.write("woops! the file has more content!...")
f.close()

f = open("pk.txt","r")

print(f.read())