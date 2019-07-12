# Scope
x = 1 # here everything is in global scope
y = 1 # here everything is in global scope

def foo():
    global y # will refer to the y in global scope

    # print(x) # this will refer to global scope x
        # but if you change x in this function - the print will crash!!

    x = 4 # will create a duplicate of x in the internal scope
    x = x + 1 # not it's ok

    print('inside the function the x is', x)

    y = y + 1 # will change the y in global scope
    print('inside the function the y is', y)

    def goo():
        print('goo')

    goo()

foo()
# goo() -- error goo is only known inside foo scope

print('outside the function the x is', x)
print('outside the function the y is', y)
