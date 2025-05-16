#  is {number}.")myself = {
#     "eyes": "blue",
#     "hair": "brown",
#     "age": 30,
#     "movies": ["pitch perfect", "big mama", "divergent"],
#     "key":{
#         "one": 1,
#         "two":2
#     }
# }

# print(myself["key"]["two"])

# my_food = {"bruger": "without cheese", "fries": "with salt", "pizza": "pepperoni"}
# new_var = my_food.get("sushi", "fried")
# #print(new_var)
# print(my_food)




# person = {
#     'first name': 'John',
#     'last_name': 'Doe',
#     'age': 30,
#     'city': 'New York'
# }
# print("First Name:", person['first_name'])
# print("Last Name:", person['last_name'])
# print("Age:", person['age'])
# print("City:", person['cuty'])



# favorite_numbers = {
#     'John': 7,
#     'Emily': 11,
#     'Sarah': 9,
#     'David': 5
# }
# for name, number in favorite_numbers.items():
#     print(f"{name}'s favorite number


rivers ={
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze':'china'
}
#print   asentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs trhough {country.title()}.")
#print name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river.title())
#print name of each country
print("\nCountries:")
for country in rivers.values():
    print(country.title())




favorite_languages = {
    'jen': 'pythn',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
people_to_poll = ['jen', 'sarah', 'david', 'emily', 'phil', 'michael']
for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you, {person.title()}, for taking the poll !")
    else:
        print(f"{person.title()}, please take the poll !")

#define dictionaries for 3 people
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

person2 = {
    'first_name': 'Emily',
    'last_name': 'Chen',
    'age': 25,
    'city': 'San Fracisco'
}

person3 = {
    'first_name': 'Michael',
    'last_name': 'Brown',
    'age': 40,
    'city': 'Chicago'

}

#store dictionaries in a list
people = [person1, person2, person3]

#Loop through the list and print everything about each person
for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")




pet1 = {
    'owner': 'John',
    'animal': 'dog'
}

pet2 = {
    'owner': 'Emily',
    'animal': 'cat'
}

pet3 = {
    'owner': 'Michael',
    'animal': 'fish'
}

pet4 = {
    'owner': 'Sarah',
    'animal': 'parrot'
    
}

#store dictionaries in a list
pets = [pet1, pet2, pet3, pet4]

#Loop through the list and print everything about each person
for pet in pets:
    print(f"This pet is a {pet['animal']} and its owner is {pet['owner']}.")