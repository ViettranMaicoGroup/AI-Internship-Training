import pandas as pd
import re
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


def load_csv(path):
    return pd.read_csv(path)


def process_sentence(sentences):
    return re.sub(r'''[~,,,`!@#$'%^&\|*()_+-={};<>.?/:'"[^0-9]''', '', sentences.lower().strip())


def new_train_test_split(X, y, test_size):
    new_X = []
    for sentence in X:
        sen = process_sentence(sentence)
        new_X.append(sen)
    new_X = np.array(new_X)
    y[y == 'negative'] = 0
    y[y == 'positive'] = 1
    X_train, X_test, y_train, y_test = train_test_split(new_X, y, test_size=test_size)
    X_train = list(X_train)
    X_test = list(X_test)
    y_train = np.array(y_train)
    y_test = np.array(y_test)

    return (X_train, X_test, y_train, y_test)


def create_pad_sequences(X, max_length, vocab_size):
    tokenizer = Tokenizer(num_words=vocab_size, oov_token='<OOV>')
    tokenizer.fit_on_texts(X)
    # word_index = tokenizer.word_index
    sequences = tokenizer.texts_to_sequences(X)
    pad_train_sequences = pad_sequences(sequences, maxlen=max_length, padding='post', truncating='post')

    return pad_train_sequences


def accuracy(y_truth, y_pred):
    count = 0
    for i in range(len(y_truth)):
        if y_truth[i] == y_pred[i]:
            count += 1
    return (count/len(y_truth))


def linear_regression(X_train, X_test, y_train, y_test, max_length, vocab_size):
    X_train_padding = create_pad_sequences(X_train, max_length, vocab_size)
    X_test_padding = create_pad_sequences(X_test, max_length, vocab_size)

    LR = LinearRegression()
    reg = LR.fit(X_train_padding, y_train)
    y_predict = reg.predict(X_test_padding)

    y_predict[y_predict > 0.5] = 1
    y_predict[y_predict <= 0.5] = 0

    acc = accuracy(y_test, y_predict)
    return acc


def logistic_regression(X_train, X_test, y_train, y_test, max_length, vocab_size):
    X_train_padding = create_pad_sequences(X_train, max_length, vocab_size)
    X_test_padding = create_pad_sequences(X_test, max_length, vocab_size)

    Log_Reg = LogisticRegression()
    y_train = y_train.astype('int')
    Log_Reg.fit(X_train_padding, y_train)

    y_predict = Log_Reg.predict(X_test_padding)

    acc = accuracy(y_test, y_predict)

    return acc


if __name__ == '__main__':
    #Load data
    df = load_csv('dataset.csv')
    # print(df.iloc[:10])

    #Shuffle data
    df_shuffled = df.iloc[np.random.permutation(df.index)].reset_index(drop=True)
    # print(df_shuffled.iloc[:10])

    #Process data to convert to vector and preprocessing
    X = df_shuffled['review']
    y = df_shuffled['sentiment']
    y[y == 'negative'] = 0
    y[y == 'positive'] = 1
    # print(new_X)
    # print(y)

    test_size = 0.2

    #split train, test data
    X_train, X_test, y_train, y_test = new_train_test_split(X, y, test_size=test_size)
    print(X_train)


    #Initialize constant
    max_length = 160
    string_ = ''
    for i in X_train:
        string_ += i
    print(len(set(string_.split(' '))))
    vocab_size = len(set(string_.split(' ')))

    #Aplly Linear Regression to classification
    print(X_train)
    lr_acc = linear_regression(X_train, X_test, y_train, y_test, max_length=max_length, vocab_size=vocab_size)
    print(f"Linear Regression Algorithm's accuracy: {lr_acc}")

    # Aplly Logistic Regression to classification
    lg_acc = logistic_regression(X_train, X_test, y_train, y_test, max_length=max_length, vocab_size=vocab_size)
    print(f"Logistic Regression Algorithm's accuracy: {lg_acc}")



