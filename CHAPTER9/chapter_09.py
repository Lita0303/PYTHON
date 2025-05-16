# Class Myself:
    
#     def___init__(self, name, age, occupation)
        
#         self.name = name
#         self.age = age
#         self.occupation = occupation
#     def introduce(self):
#         print(f"Hello, my name is {self.name} and I am a {self.occupation}.")
# #create an instance of myself class
# me = Myself("John Doe", 21, "Software Developer")




class Restuarant:
    def __init__(self, restuarant_name, cuisine_type):
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type
    
    def describe_restuarant(self):
        print(f"{self.restuarant_name} is a {self.cuisine_type} restuarant.")
    def open_restuarant(self):
        print(f"{self.restuarant_name} is now open!")
    
restuarant = Restuarant('Tasty Bites', 'Italian')

print(restuarant.restuarant_name)
print(restuarant.cuisine_type)

restuarant.describe_restuarant()
restuarant.open_restuarant()

class Restuarant:
    def __init__(self, restuarant_name, cuisine_type):
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type
    
    def describe_restuarant(self):
        print(f"{self.restuarant_name} is a {self.cuisine_type} restuarant.")
    def open_restuarant(self):
        print(f"{self.restuarant_name} is now open!")
    
restuarant1 = Restuarant('Tasty Bites', 'Italian')
restuarant2 = Restuarant('Sushi House', 'Japanese')
restuarant3 = Restuarant('Taco Fiesta', 'Mexican')

restuarant1.describe_restuarant



class User:
    def __init__ (self, first_name, last_name, username, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
    def describe_user(self):
        print(f"User Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")
    
user1 = User('Litamile', 'Vimbi', 'Litamza', 'litamile500@gmail.com', 21)
user2 = User('Jabulani', 'Mpapane','Jabz', 'jay2205@gmail.com', 22)
user3 = User('Alwande', 'Sheleni', 'Alwa', 'alwa17@gmail.com', 17)

users = [user1, user2, user3]
for user in users:
    user.describe_user()
    print()


    







