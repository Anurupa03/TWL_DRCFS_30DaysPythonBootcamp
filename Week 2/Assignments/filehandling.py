'''
Write a Python function called read_file() that takes a single parameter
filename, and opens the specified file in read-only mode. 
The function should read the entire contents of the file and return the contents as a string.
'''

def read_file(filename):
    
    file = open(filename,"r").read()
    return file

contents = read_file("my_file.txt")
print(contents)  # Output: "Hello, world!\nI just did my first Assignment of week 2."
