
# FILES

f1 = open('c:/itay/hello.txt') # open file for read - default

print(f1)

listOfLines = f1.readlines() # not for very large files

for line in listOfLines:
    print(line[:-1])

print(listOfLines) # ['hello\n', 'python\n', 'world!']

f1.seek(0) # moves file cursor to begining of the file

for line in f1.readlines():
    print(line[:-1])

f1.close()

#for line in f1.readlines():
#    print(line)
