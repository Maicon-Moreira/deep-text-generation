import keras
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Activation, Dropout

model = Sequential([
  Embedding(15000, 100, input_length=10),
  Dropout(0.3),
  LSTM(200),
  Dropout(0.3),
  Dense(200),
  Dropout(0.3),
  Dense(15000),
  Activation('softmax')
])
model.summary()
model.compile(loss='categorical_crossentropy',optimizer='adam')

model.save('model.h5')