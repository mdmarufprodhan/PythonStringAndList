#create list
numbers = [1,2,3,4,5]
#print(numbers)
#Using a constructor
numbers = list((1,2,3.4,6,7))
#print(numbers)
fruits = ['Apple','Oranges', 'Grapes', 'Pears']
#nget values
print(fruits[1])

#get len
print(len(fruits))

#Append to ist
fruits.append('Mangos')
#print(fruits)

#Remove from list
fruits.remove('Grapes')
#print(fruits)
#Insert into position
fruits.insert(2,'Strawberries')
#print(fruits)

#Remove from posotion
fruits.pop(3)


#Reverse list
fruits.reverse()
fruits.sort()

print(fruits)

