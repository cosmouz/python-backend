import os

file_name = input('Enter the name for the new file: ')

while os.path.exists(f"{file_name}.txt"):
    file_name = input('A file with this name already exists. Please provide another name: ')

# File doesn't exist, create a new one
with open(f"{file_name}.txt", 'w') as f:
    f.write('Salom')

print(f"File '{file_name}.txt' has been created successfully!")
