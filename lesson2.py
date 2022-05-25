#a dictionary is a collection of key value pair
#syntax: dictionary = ['key':'value']
colours= {'colours':'red'}
vehicle={'type':'toyota','plate_number':'qwe234y'}
print(type(colours))
#accesing values in dictionaries
print(vehicle['type'])
#you can acess value of an element using a key
person={'name':'deno','gender':'male','phone_number':'0721570905','location':'nairobi'}
person['age']='21'
#print(type(person))
#print(person)
#looping over dictionaries
for key,value in person.items():
    print(f"{key}:{value}")
