import json

my_details = {
    'name': 'John Doe',
    'age': 29,
    'title': "this is a news headline",
    'author': 'This is a person',
    'paragraph': ["pa", "pb", "pc"]
}

with open('personal.json', 'w') as json_file:
    json.dump(my_details, json_file)