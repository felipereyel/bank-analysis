import csv
import math
import operator


def load_data(filename, split_training, training_set=[], test_set=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        lines_training = math.floor((len(dataset)) * split_training)

        for x in range(len(dataset)):
            if x < lines_training:
                training_set.append(dataset[x])
            else:
                test_set.append(dataset[x])


def get_euclidean_distance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(distance)


def get_k_neighbors(training_set, test_instance, k):
    distances = []
    length = len(test_instance) - 1
    for x in range(len(training_set)):
        dist = get_euclidean_distance(training_set[x], test_instance, length)
        distances.append((training_set[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def get_frequent_class(neighbors):
    class_votes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1
    sortedVotes = sorted(class_votes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def get_accuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0


def main():
    training_set = []
    test_set = []
    split_training = 0.67
    load_data('../dataset/iris.data', split_training, training_set, test_set)
    predictions = []
    k = 2
    for x in range(len(test_set)):
        neighbors = get_k_neighbors(training_set, test_set[x], k)
        result = get_frequent_class(neighbors)
        predictions.append(result)
        print('predicao=' + repr(result) + ' > valor_real=' + repr(test_set[x][-1]))
    accuracy = get_accuracy(test_set, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')


main()
