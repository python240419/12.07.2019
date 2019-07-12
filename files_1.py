
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
    # because of the with --> here the open will be closed

with open('c:/itay/new.txt', 'w') as f1:
    f1.write("Hello new file!!")

# create a file with your name
# create a file and copy the previous file into it and add your name
#   at the end
# harder solution :
with open('c:/itay/new2.txt', 'w') as f1:
    for line in open('c:/itay/hello.txt'):
        f1.write(line)

with open('c:/itay/new2.txt', 'a') as f1:
    f1.write("\nitay")

# easier solution : 
f1 = open('c:/itay/hello.txt') # open file for read - default
listOfLines = f1.readlines()
with open('c:/itay/new2.txt', 'w') as f1:
    for line in listOfLines:
        f1.write(line)
    f1.write("itay")        
