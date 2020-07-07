from unicodedata import normalize


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


with open('book.txt', 'r') as file:
    book = file.read()

book = book.lower()
book = book.replace('\n', ' ')
book = book.replace('\x0c', ' ')
book = book.replace('\x0b', ' ')

book = book.replace('.', ' .')
book = book.replace(',', ' ,')
book = book.replace('?', ' ?')
book = book.replace('!', ' !')
book = book.replace(':', ' :')
book = book.replace(';', ' ;')

book = book.replace('-', ' - ')

book = book.replace('“', '“ ')
book = book.replace('”', ' ”')
book = book.replace('‘', '‘ ')
book = book.replace('’', '’ ')
book = book.replace('”', ' ”')
# ‘
book = book.replace('(', '( ')
book = book.replace(')', ' )')

book = remover_acentos(book)

with open('formated_book.txt', 'w') as file:
  file.write(book)

# print(book[:2000])