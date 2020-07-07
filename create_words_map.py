import json


def order_dictionary_by_value(_dict):
    return {k: v for k, v in sorted(_dict.items(), key=lambda item: item[1], reverse=True)}


with open('formated_book.txt', 'r') as file:
    book_words = file.read().split(' ')

counted_words = {}

for word in book_words:
    if word in counted_words.keys():
        counted_words[word] += 1
    else:
        counted_words[word] = 1


ordered_counted_words = order_dictionary_by_value(counted_words)

print(len(book_words), 'palavras')
print(len(ordered_counted_words), 'palavras diferentes')


selected_words = list(ordered_counted_words.keys())[:15000]

word_map = {selected_words[i]: i for i in range(len(selected_words))}
word_map_reversed = {i: selected_words[i] for i in range(len(selected_words))}


book_words_mapped = []

for word in book_words:
    if word in word_map.keys():
        book_words_mapped.append(word_map[word])

# print(book_words_mapped)


with open('ordered_counted_words.txt', 'w') as file:
    file.write(json.dumps(ordered_counted_words))

with open('word_map.txt', 'w') as file:
    file.write(json.dumps(word_map))

with open('word_map_reversed.txt', 'w') as file:
    file.write(json.dumps(word_map_reversed))

with open('book_words_mapped.txt', 'w') as file:
    file.write(json.dumps(book_words_mapped))
