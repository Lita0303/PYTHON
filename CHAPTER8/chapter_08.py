# def my_function(name, surname):
#     print("Hello " + name + " " + surname)
# my_function(name = "Litamile", surname = "Vimbi") #same function with different arguments.

# def my_function(address, status):
#     print("I live at " + " " + address + " and I am currently" + " "  + status)
# my_function("624 Smit Street", "employed")

def display_message():
    print("Hi everyone, we are going going to be starting Python Projects next week !")
display_message()

def favorite_book(title):
    print("My favorite book of all time is" + " " + title)
favorite_book(title = "After.")

def make_shirt(size = 'Large', text = 'I Love Python'):
    print("The shirt that is being made for me is a size" + " " + size + " " + "with a writing that says," + " " + text + " " + "on it.")
make_shirt()
make_shirt(size = 'Medium')
make_shirt(size = 'Small', text ='Python is cool!')

def make_sandwich(*items):
    print("You're ordering a sandwich with the following itemas:")
    for item in items:
        print(f"-{item}")
    
make_sandwich('turkey', 'avocado', 'tomato')
make_sandwich('ham', 'cheese')
make_sandwich('roast beef', 'lettuce', 'mayo', 'mustard', 'pickles')


