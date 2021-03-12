var = 9          # global variable
a = True
newvar = 23
def fun(x):
    global a
    a = 7 # local variable

    if x == 5:
        return True

def otherFun():
    newvar = 5   #local variable
    print(newvar)

fun(2)
print(a)
