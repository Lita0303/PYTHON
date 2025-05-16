#Files
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
with open('example.txt', 'w') as file:
    file.write('Hello, world!')
with open('example.txt', 'a') as file:
    file.write('\nThis is a new line.')


#Exceptions (Try-Except block)
try:
    x = 5 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')


#Exception (Handling file not  found)
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('The file does not exist.')