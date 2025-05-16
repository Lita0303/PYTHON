#create an array and make a for loop
# my_list = ["apples", "oranges", "grapes", "peaches", "strawberries"]
# for fruit in my_list:
#     print(f"I am craving {fruit}, how much does it cost?")
# print("I'll have all of them please.")




# # range(): from 10 to 20 count in 2's
# for each_number in range(10, 20, 2 ):
#     print(each_number)

# my_new_list = list(range(0,100, 5))
# print(my_new_list)



#create a list of your 3 favorite pizzas and print a message for each pizza using a for loop.
favorite_pizza = ["chicken and mushroom", "pepperoni", "three cheese"]
for pizza in favorite_pizza:
    print(f"{favorite_pizza[0]}, must be creamy to taste its best !")
    print(f"{favorite_pizza[1]}, must have extra cheese for it to taste its best !")
    print(f"{favorite_pizza[2]}, must be hot for it to taste its best !")
#add a line at the end of the program
print("These are my favorite pizzas so my opinion is the best.")

#use a for loop to print the numbers from 1 to 20, inclusive
for value in range(1, 21):
    print(value)

#make a list of numbers from one to one million, use min() and max() to ensure list starts at one end end at a million, use sum() to add a million numbers
numbers = list(range(1, 1000001))
print(numbers)
min(numbers)
max(numbers)
sum(numbers)

#print odd numbers from 1 to 20 
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

#list of 10 cubesfrom 1 to 10 using a for loop to print the value of each cube
cubes = []
for value in range (1, 11):
    cubes.append(value ** 3)
print(cubes)

#create a list and and slice it. 
my_list = ["apples", "oranges", "grapes", "peaches", "strawberries"]
print(f"The first three items in the list are: {my_list[0:3]}")
print(f"The itesm from the middle of the list are: {my_list[1:4]}")
print(f"The last three items in the list are: {my_list[2:]}")

#store five food in a tuple
foods = ("sushi", "burger", "pizza", "fries")
print(foods)

