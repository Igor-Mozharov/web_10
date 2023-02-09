from mongoengine import connect, Document
from mongoengine.fields import StringField, DateField, ListField, ReferenceField

con = connect(host=f'mongodb+srv://Igor8282:password5@cluster0.tvqcfdh.mongodb.net/?retryWrites=true&w=majority')


class Author(Document):
    fullname = StringField(required=True)
    born_date = DateField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)


class Quotes(Document):
    tags = ListField(required=True)
    author = ReferenceField(Author)
    quote = StringField(required=True)


def select_authors():
    authors_list = []
    for autor in Author.objects:
        authors_list.append({
            'fullname': autor['fullname'],
            'born_date': autor['born_date'],
            'born_location': autor['born_location'],
            'description': autor['description']
        })
    return authors_list


def select_quotes():
    quotes_list = []
    for quote in Quotes.objects:
        quotes_list.append({
            'tags': quote['tags'],
            'author': quote['author'],
            'quote': quote['quote']
        })
    return quotes_list

if __name__ == '__main__':
    select_authors()
    select_quotes()