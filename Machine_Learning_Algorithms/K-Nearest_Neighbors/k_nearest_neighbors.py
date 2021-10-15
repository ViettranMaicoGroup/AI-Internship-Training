import pandas as pd
import numpy as np
import random
random.seed(8)


def euclid_distance(X,Y):
    return np.linalg.norm(X - Y)


def load_data(path):
    df = pd.read_csv(path, sep= '\t')
    df = df[['fruit_label', 'mass', 'width', 'height']]
    return np.array(df)


def train_test_split(data, test_size):
    random.shuffle(data)
    try:
        assert(test_size >= 0 and test_size <= 1)
    except Exception:
        print("Test_size must in [0, 1]")

    train_size = 1 - test_size
    limit = int(np.floor(train_size*data.shape[0]))
    trainSet = data[:limit, :]
    testSet = data[limit:, :]

    return (trainSet, testSet)


def knn_algorithm(X, point, k):
    distances = []
    for item in X:
        distances.append({
            'label' : item[0],
            'value' : euclid_distance(item, point)
        })

    distances.sort(key= lambda x :  x['value'])
    labels = [item['label'] for item in distances]
    print(labels[:k])
    return labels[:k]


def find_most_occur(arr):
    labels = set(arr)
    ans = ''
    max_occur = 0

    for label in labels:
        num = arr.count(label)
        if num > max_occur:
            max_occur = num
            ans = label

    return ans


def acc(trainSet, testSet, k):
    right_ans = 0
    for item in testSet:
        for i in item:
            if i == None:
                continue
        #apply knn to find k labels of k nearest point
        knn = knn_algorithm(trainSet, item, k)
        #find the most occur labels in that
        answer = find_most_occur(knn)
        right_ans += item[0] == answer
    acc = right_ans/len(testSet)
    return acc


if __name__ == '__main__':
    #load and review data
    data = load_data('fruits.txt')
    print(data)
    print(data.shape)

    #split data into train set and test set
    trainSet, testSet = train_test_split(data, 0.2)
    print(trainSet)
    print(trainSet.shape, testSet.shape)

    #Evaluate accuracy of algothms
    print(f'Accuracy: {acc(trainSet, testSet, 3)}')