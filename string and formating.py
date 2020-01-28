name = 'Maruf'
age = 21
#Concatenate
print('Hello I am ' + name + '  and I am ' + str(age))

#String formating

#Argument by position
print('{},{},{}'.format('a','b', 'c'))

#print('{1},{2},{0}'.format('a','b', 'c'))
#Argument by name
print('My name is {name} and i  am {age}'.format(name = name, age = age))
#F- string
print(f'My name is {name} and I am {age}')
#String method
s = 'Hello  there  world'

#Capitilize  Firt letter
print(s.capitalize())
print(s.upper())
print(s.swapcase())
#String length

print(len(s))
#Replace
print(s.replace('world' , 'everyone'))
#count
sub = "M"
print(s.count(sub))

#Starts with
print(s.startswith('hello'))
#Ends with
print(s.split())
#Finf position
print(s.find('r'))

#Is All nummeric
print(s.isnumeric())
#Is alphabetic
print(s.isalpha())