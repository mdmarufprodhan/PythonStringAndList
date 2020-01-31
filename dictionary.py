#Simple dictionary

person = {
    'first_name': 'Maruf',
    'last_name':'Prodhan',
    'age': 30
}
print(person)


#acces value
print(person['first_name'])
print(person.get('last_name'))

#add key value

person ['phone'] = '01766380481'
print(person.keys())
print(person.items() )




#Make Copy
perpson2 = person.copy()
perpson2['city'] = 'Bogra'
print(perpson2)




#Remove item
del(person['age'])
person.pop('phone')
print(person)

#Clear

person.clear()

#get length
print(len(perpson2))



#list of dictionary

people = [

    {'name': 'Parven', 'age': 22},
{'name': 'Sharan', 'age': 21}

]
print(people[1]['name'])


