fruits = ['apples', 'pears', 'strawberries']
text = 'Hello I am Jay'

print(text[ : : ]) #start, stop, step

print(text[::3])

print(fruits[::])

fruits.append('blueberries')
print(fruits)

fruits[0:0] = ['banana']
print(fruits)