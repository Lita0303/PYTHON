#create a list of all your friends, then call them 1 at a time.
names = ["Palesa K", "Lisabahle", "Sukoluhle", "Palesa K", "Zoe"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])


#write the same message to all your friends but personalise it for each person
message = f"Dear {names[0]}, you are loved!"
print(message) 
message = f"Dear {names[1]}, you are loved!"
print(message)
message = f"Dear {names[2]}, you are loved!"
print(message)
message = f"Dear {names[3]}, you are loved!"
print(message)
message = f"Dear {names[4]}, you are loved!"
print(message)

#you forgot to add your male friends add one in the middle, another at the beginning and one at the end
names.append("Siphelele")
names.insert(0,"Liyema")
names.insert(3,"Jabulani")
print(names)



#remove friends one at a time in our list
print(names.pop())
print(names)
print(names.pop())
print(names)
del names[0]
print(names)
names.remove("Jabulani")
print(names)

#a list of people in your life, make it in alphabetical order, show that the list order was changed, print your list in reverse order
people = ["mom", "dad", "sister1", "sister2", "brother"]
print(people)
people.reverse()
print(people)
people.sort()
print(people)
print(people)