#write a series of conditional tests, print a statement for each tect and your prediction for results of each test
car = "bmw"
print("Is car == 'bmw' ? I predict True.")
print(car == "bmw")

print("\nIs car == 'BMW' ? I predict False.")
print(car == "BMW")


score = 90
print("\nIs score >= 80  ? I predict True.")
print(car == "AUDI")

print("\nIs score <= 80 ? ? I predict False.")
print(car == "audi")


is_logged_in = True
print("\nIs user logged in ? I predict True.")
print(is_logged_in)

print("\nIs user not logged in  ? I predict False.")
print(is_logged_in)

colors = ["red", "green", "yellow"]
print("\nIs 'yellow' in colors ? I predict True.")
print("yellow" in colors)

print("\nIs 'blue' in colors ? I predict False.")
print("blue" in colors)

numbers = [1, 2, 3, 4, 5]
print("\nIs len(numbers) == 5 ? I predict True.")
print(len(numbers == 5))

print("\nIs len(numbers) == 3 ? I predict False.")
print(len(numbers == 3))

#writing an if statement to test whether the aliens's color is green, if it is print a simple message
#passing the if test
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!")

#failing the test
alien_color = "red"
if alien_color == "green":
    print("You ust earned 5 points!")



#write an if-else chain
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!")
else:
    print("You just earned 10 points")

alien_color = "red"
if alien_color == "green":
    print("You ust earned 5 points!")
else:
    print("You just earned 10 points!")

#Turn if-else chain to and if-elifelse chain
if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points")
else:
    print('You earned 15 points!)')

alien_color = "red"
if alien_color == "green":
    print("You ust earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You earned 15 points!")



#write an if-else chain that determines a person's stage of life with a message for each person stages.

age = 25
if age < 2:
    print("You are a baby!")
elif age < 4:
    print("You are a todler!")
elif age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are an adult!")
else:
    print("You are an elder!")

#make a list of 5 admins, print a greeting to each user after logging into a website

usernames = ["admin", "jaden", "sarah", "mike", "emily"]
for username in usernames:
    if username == "admin":
        print(f"Hello {username.tile()} would you like to see a status report ?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again")





