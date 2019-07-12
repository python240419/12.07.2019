
# FILES
f1 = open('c:/itay/hello.txt') # open file for read - default

print(f1)
print(f1.tell()) # tell me where i am in the file
listOfLines = f1.readlines() # read all the lines into a list
                             # not for very large files

print(f1.tell()) # tell me where i am in the file
for line in listOfLines:
    print(line, end="")

print('\n', listOfLines) # ['hello\n', 'python\n', 'world!']

f1.seek(1) # moves file cursor to begining of the file

for line in f1.readlines():
    print(line, end="")

f1.close()

#for line in f1(): -- automatically does readlines()
#    print(line)

with open('c:/itay/hello.txt') as f1:
    for line in f1:
        print(line, end="")
    # because with -- here the open will be closed
