import keras
import json
import numpy as np

model = keras.models.load_model('model.h5')

with open('book_words_mapped.txt', 'r') as file:
    book_words_mapped = json.loads(file.read())
with open('word_map.txt', 'r') as file:
    word_map = json.loads(file.read())
with open('word_map_reversed.txt', 'r') as file:
    word_map_reversed = json.loads(file.read())

def numbers_to_phrase(numbers):
  return ' '.join([word_map_reversed[str(number)] for number in numbers.tolist()])

def phrase_to_number(phrase):
  array = []
  for word in phrase.split(' '):
    if word in word_map.keys():
        array.append(word_map[word])
    else:
      print('"', word, '"', 'nao existe')
  return array


xs = []
ys = []

for i in range(len(book_words_mapped) - 21):
    x = [*book_words_mapped[i:(i + 20)]]
    xs.append(x)

    y = [book_words_mapped[(i + 21)]]
    ys.append(y)

xs = np.array(xs)
ys = np.array(ys)
# ys = keras.utils.to_categorical(ys, 15000)

print(xs.shape)
print(ys.shape)


phrase = 'ela tentava andar para casa , pensando nisso pesquisadores desenvolveram'

array = phrase_to_number(phrase)

for a in range(20):
  x = np.array([array[-10:]])
  y = np.argmax(model.predict(x)[0])

  array.append(y)

print(numbers_to_phrase(np.array(array)))
