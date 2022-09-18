#Loading the IMDB dataset

from tensorflow.keras.datasets import imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

#Displaying the training data first entry

train_data[0]
