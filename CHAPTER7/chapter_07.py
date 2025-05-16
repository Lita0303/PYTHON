# full_name = input("What is your name first name?")
# print(f"Hello {full_name}")
      
# full_name += input("What is your last name ?")
# print(f"Hello {full_name}")

# age = input("What is your age ?")
# if int(age) > 18:
    # print("Have a beer?")
# elif int(age) < 18:
    # print("Not today.")



#while loops
# number = 0

# while number < 10:
#     print(number)
#     number += 1

# print("Finished")







def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("Alice in Wonerland")

def make_shirt(size, message):
    print(f"This shirt is a size {size} and has the message '{message}' printedon it.")
make_shirt(f"Medium", "I love Python")
make_shirt(size = "Large",  message = "Code is poetry")

def make_shirt(size = "Large", message = "I love Python"):
    print(f"This shirt is a size {size} and has the message '{message}' printed on it.")
make_shirt()
make_shirt(size = "Medium")
make_shirt(size = "Small", message = "Code is fun")


def describe_city(city, country = "South Africa"):
    print(f"{city} is in {country}.")
describe_city("Port Elizabeth")
describe_city("Cape Town")
describe_city("Tokyo", "Japan")

def make_album(artist, title, songs = None):
    album = {
        'artist': artist,
        'title': title
    }
    if songs is not None:
        album['songs'] = songs
    return album
album1 = make_album("Jhene Aiko", "Chilombo")
album2 = make_album("Summer Walker", "Over It")
album3 = make_album("Giveon", "When It's All Said and Done")

print(album1)
print(album2)
print(album3)


def make_album(artist, title, songs = None):
    album = {
        'artist': artist,
        'title': title
    }
    if songs is not None:
        album['songs'] = songs
    return album
while True:
    print("\nEnter album information (or 'q' to quit):")
    artist = input("Artist: ")
    if artist.lower() == 'q':
        break
    title = input("Title: ")
    if title.lower() =='q':
        break
    songs = input("Number of songs (optional): ")
    if songs.lower() == 'q':
        break
    if songs:
        album = make_album(artist, title, int(songs))
    else:
        album = make_album(artist, title)
    print(album)

