import keras
import json
import numpy as np

model = keras.models.load_model('model.h5')

with open('book_words_mapped.txt', 'r') as file:
  book_words_mapped = json.loads(file.read())

xs = []
ys = []

for i in range(len(book_words_mapped) - 21):
  x = [*book_words_mapped[i:(i + 10)]]
  xs.append(x)

  y = [book_words_mapped[(i + 11)]]
  ys.append(y)

xs = np.array(xs)
ys = np.array(ys)

print(xs.shape)
print(ys.shape)

for i in range(10):
  xs_array = []
  ys_array = []

  for i in range(10000):
    random_i = np.random.randint(len(xs))
    xs_array.append(xs[random_i])
    ys_array.append(ys[random_i])

  xs_array = np.array(xs_array)
  ys_array = np.array(ys_array)
  ys_array = keras.utils.to_categorical(ys_array, 15000)

  print(xs_array.shape)
  print(ys_array.shape)

  model.fit(xs_array, ys_array, epochs=1)

model.save('model.h5')