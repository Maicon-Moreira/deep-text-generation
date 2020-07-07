with open('book.txt', 'r') as file:
  book_words = file.read().split(' ')

print(book_words[:100])