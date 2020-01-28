name = 'Maruf'
age = 21

#Concatente
print('Hello I am ' + name + ' and i am ' + str(age))

#sring formating

#Argument nby position
print('{} , {}, {},'.format('a', 'b', 'c'))
print('{1} , {2}, {0},'.format('a', 'b', 'c'))

#Argument by name
print('My name is {name} and i am {age}' .format(name = name , age = age))
# F-string
#print(f'My name is {name} and I am {age}')
#String methods
s = 'Hello there world'

#capitalze first letter


print(s.capitalize())
#Make all uppercase'

print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
print(s.replace('world', 'everyone'))

sub ="H"
print(s.count(sub))
