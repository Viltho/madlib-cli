import re

def read_template(template_path):
    try:
        with open(template_path) as f:
            return f.read().strip()
    except FileNotFoundError:
        print('Error: File not found')
        raise FileNotFoundError
    
def parse_template(template):
    global language_parts
    pattern = r'{([^}]*)}'
    language_parts = re.findall(pattern, template)
    language_parts_removed = re.sub(pattern, '{}', template)
    return language_parts_removed, tuple(language_parts)

def prompt_user_for_input(language_parts):
    user_input = []
    for part in language_parts:
        user_input.append(input(f"Enter a {part}: "))
    return user_input

def merge(template, language_parts):
    try:
        return template.format(*language_parts)
    except KeyError as e:
        print(f'Error: missing key {e} in user input')
        return None
