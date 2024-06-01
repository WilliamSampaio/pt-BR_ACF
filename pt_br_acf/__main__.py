import json


from pt_br_acf import BASE_URL
from pt_br_acf.functions import get_books_slug, get_soup, zip_bible

# rename_files()
# print('oi!')
# sys.exit()

books = get_books_slug()
if books is None:
    raise Exception

for book_index in range(0, len(books)):

    for chapter in range(1, 151):

        data = {
            'book': books[book_index][0],
            'chapter': chapter,
            'verses': [],
        }

        soup = get_soup(
            BASE_URL
            + 'acfonline-versos?livro={}&capitulo={}'.format(
                books[book_index][1],
                str(chapter),
            )
        )

        if soup is None:
            break

        verses = soup.find_all(attrs={'class': 'verse-text'})

        for verse in verses:

            data['verses'].append(''.join([str(a) for a in list(verse)]))

        with open(
            f'data/{str(book_index + 1).zfill(2)}_{chapter}.json', 'w'
        ) as f:
            f.write(json.dumps(data))

        print(books[book_index][0], chapter)

zip_bible('pt-BR_ACF')
