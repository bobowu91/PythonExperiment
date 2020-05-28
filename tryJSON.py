import json

my_details = {
    'name': 'John Doe',
    'age': 29,
    'title': "this is a news headline",
    'author': 'This is a person',
    'paragraph': ["pa", "pb", "pc"]
}
''' 
with open('personal.json', 'w') as json_file:
    json.dump(my_details, json_file)
    
with open("mobos.json", "w") as outfile:
    for news_article in wsj:
        json.dump(news_article, outfile)
        outfile.write('\n')

with open("pywsj_content.json", "w") as outfile:
    for news_article in journal:
        json.dump(news_article, outfile)
        outfile.write('\n')
 '''       
with open("pywsj_content.json") as f:
    data = f.read()
    wsj = json.load(data)