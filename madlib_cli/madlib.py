# import re
# import time
# import os

# folder_path = "assets"
# files = os.listdir(folder_path)
# i = 0
# array_of_files = []

# print("Welcome to Madlibs! Please wait while we load your files...")
# for file in files:
#     i += 1
#     array_of_files.append({i: file})
#     print(f"{i}: {file}")
    
# my_dict = {}

# for item in array_of_files:
#     my_dict.update(item)

# user_input = ""
# while user_input not in my_dict:
#     try:
#         user_input = int(input("Please select your file to start the Madlib: "))
#         template_path = my_dict[user_input]
#         continue
#     except KeyError:
#         print("Invalid file number")

# template_path = f"{folder_path}/{my_dict[user_input]}"

# def read_template(template_path):
#     try:
#         with open(template_path) as f:
#             return f.read().strip()
#     except FileNotFoundError:
#         print('Error: File not found')
#         return None
    
# ### Parsing from template
# def parse_template(template):
#     global language_parts
#     pattern = r'{([^}]*)}'
#     language_parts = re.findall(pattern, template)
#     language_parts_removed = re.sub(pattern, '{}', template)
#     return language_parts_removed, tuple(language_parts)

# ### Body parts input for the template
# def prompt_user_for_input(language_parts):
#     user_input = []
#     for part in language_parts:
#         user_input.append(input(f"Enter a {part}: "))
#     return user_input

# ### Merging from template
# def merge(template, language_parts):
#     try:
#         return template.format(*language_parts)
#     except KeyError as e:
#         print(f'Error: missing key {e} in user input')
#         return None

# ### entering data for template
# read = input("Would you like to play the Madlibs and fill in the blanks ? (y/n): ")
# if read == 'y':
#     template, language_parts = parse_template(read_template(template_path))
#     user_input = prompt_user_for_input(language_parts)
#     merged_template = merge(template, user_input)
#     print(f"Listen Listen to the Madlib: \n{merged_template}")
# else:
#     pass

import re
import os

def read_template(template_path):
    try:
        with open(template_path) as f:
            return f.read().strip()
    except FileNotFoundError:
        print('Error: File not found')
        return None

def parse_template(template):
    language_parts = re.findall(r'{([^}]*)}', template)
    return re.sub(r'{([^}]*)}', '{}', template), tuple(language_parts)

def prompt_user_for_input(language_parts):
    return [input(f"Enter a {part}: ") for part in language_parts]

def merge(template, language_parts):
    try:
        return template.format(*language_parts)
    except KeyError as e:
        print(f'Error: missing key {e} in user input')
        return None

folder_path = "assets"
files = os.listdir(folder_path)
my_dict = {i+1: file for i, file in enumerate(files)}

print("Welcome to Madlibs! Please wait while we load your files...")
for i, file in my_dict.items():
    print(f"{i}: {file}")

while True:
    user_input = input("Please select your file to start the Madlib: ")
    if user_input.isdigit() and int(user_input) in my_dict:
        break
    print("Invalid file number")

template_path = f"{folder_path}/{my_dict[int(user_input)]}"
template = read_template(template_path)

if template:
    template, language_parts = parse_template(template)
    user_input = prompt_user_for_input(language_parts)
    merged_template = merge(template, user_input)
    if merged_template:
        print(f"Listen Listen to the Madlib: \n{merged_template}")
