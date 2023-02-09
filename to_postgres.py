import pg8000.native
from from_mongo import select_quotes, select_authors

con = pg8000.native.Connection('postgres', password='5747144')

def add_authors():
    for a in select_authors():
        con.run('INSERT INTO quotesapp_author (fullname, born_date, born_location, description) VALUES (:fullname, :born_date\
        , :born_location, :description)', fullname=a['fullname'], born_date=a['born_date'], born_location=a['born_location']\
    ,description=a['description'])


def add_quotes():
    for au in con.run('SELECT id, fullname FROM quotesapp_author'):
        for q in select_quotes():
            if au[1] == q['author'].fullname:
                con.run('INSERT INTO quotesapp_quote (tags, quote, author_id) VALUES (:tags, :quote, :author_id)', tags=q['tags'],\
                        quote=q['quote'], author_id=au[0])

if __name__ == '__main__':
    add_authors()
    add_quotes()
    con.close()