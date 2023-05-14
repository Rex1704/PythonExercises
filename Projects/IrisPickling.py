def pickledata(listdata):
    import pickle
    iris_pickle_file = "iris.pkl"
    iris_file = open(iris_pickle_file, "wb")
    pickle.dump(listdata, iris_file)
    return iris_pickle_file


def unpickledata(pkl_file):
    import pickle
    file_iris = open(pkl_file, "rb")
    unpickled_iris = pickle.load(file_iris)
    return unpickled_iris


if __name__ == '__main__':
    import requests
    iris_Data = requests.post("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
    parsed_Iris_Data = iris_Data.text.split("\n")
    parsed_Iris_Data = list(map(lambda x: x.split(","), parsed_Iris_Data))
    file = pickledata(parsed_Iris_Data)
    iris_unpickled = unpickledata(file)
    if parsed_Iris_Data == iris_unpickled:
        print('pickling and unpickling successfully done!!')
        print(iris_unpickled)
