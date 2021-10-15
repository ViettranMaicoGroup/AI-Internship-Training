import csv
import numpy as np
import math

def load_data(path):
    f = open(path, "r")
    data = csv.reader(f) #csv format
    data = np.array(list(data)) #convert to matrix
    data = data[1:, :]
    # data = np.delete(data, 0, 0)
    # data = np.delete(data, 0, 1)
    np.random.shuffle(data)
    f.close()
    trainSet = data[:100]
    testSet = data[100:]
    return (trainSet, testSet)


def calcDistance(pointA, pointB, numofFeature=4):
    tmp = 0
    for i in range(numofFeature):
        tmp += (float(pointA[i])- float(pointB[i])) **2
    return math.sqrt(tmp)


def k_nearest_neighbor(trainSet, point, k):
    distances = []
    for item in trainSet:
        distances.append({
            "label": item[-1],
            "value": calcDistance(item, point)
        })
    distances.sort(key=lambda x:x["value"])
    labels = [item["label"] for item in distances]
    return labels[:k]


def find_most_occur(arr):
    labels = set(arr)
    ans = ""
    max_occur =  0
    for label in labels:
        num = arr.count(label)
        if num > max_occur:
            max_occur = num
            ans = label
        return ans


if __name__ == "__main__":
    trainSet, testSet = load_data("iris.csv")
    num_right_ans = 0
    for item in testSet:
        knn = k_nearest_neighbor(trainSet, item, 5)
        ans = find_most_occur(knn)
        num_right_ans += (item[-1] == ans)
        print(f"Label: {item[-1]} -> Predicted: {ans}")
    print(f"Accuracy: {num_right_ans/len(testSet)}")