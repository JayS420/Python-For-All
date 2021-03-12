"""
while condition == True:
    do this
    break
"""
loop = True
while loop:
    name = input("insert anything")
    if name == 'stop':
        loop = False
        break
