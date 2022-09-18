#Loading the IMDB dataset

from tensorflow.keras.datasets import imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

#Displaying first entries of training data and its size

train_data[0]
train_labels[0]
max([max(sequence) for sequence in train_data])
