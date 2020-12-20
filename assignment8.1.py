import os # importing os
os.system('cls') # clearing the screen
directory = input('What is the name of the directory you would like to add a file to:\n') # prompting the user for the name of their directory
os.system('cls') # clearing the screen
file_name = input('name the file:\n') # prompting the user for the name of the file they would like to save
if(not os.path.isdir(directory)): # checking to see if the directory exsists
    os.mkdir(directory) # creating the directory of their choice if it does not exsist

os.system('cls') # clearing the screen
name = input("name:\n") # prompting for their name
address = input('address:\n') # prompting for their address
cell = input('phone number:\n') # prompting for their phone number
os.system('cls') # clearing the screen
os.chdir(directory) # changing directories to the one just created
file = open(file_name, 'a') # creating / opening a file
file.write(f'{name}, {address}, {cell}') # writing to that file
file.close() # closing the file
os.system(f'notepad {file_name}')
