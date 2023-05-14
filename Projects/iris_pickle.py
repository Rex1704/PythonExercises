"""I here done some pickling and unpickling of iris data taken from uci ml website.
 yes the most popular one "irisdata"  """

def pickledata(listdata):
    """pickle the data into a file and returns it"""
    iris_pickle_file = "iris.pkl"
    iris_file = open(iris_pickle_file, "wb")
    pickle.dump(listdata, iris_file)
    return iris_pickle_file


def unpickledata(pkl_file):
    """unpickle the pickled file and return the data"""
    file_iris = open(pkl_file, "rb")
    unpickled_iris = pickle.load(file_iris)
    return unpickled_iris


if __name__ == '__main__':
    import requests
    import pickle

    iris_Data = requests.post(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", timeout=0.5)
    parsed_Iris_Data = iris_Data.text.split("\n")
    parsed_Iris_Data = list(map(lambda x: x.split(","), parsed_Iris_Data))
    FILE_PICKLE = pickledata(parsed_Iris_Data)
    iris_unpickled = unpickledata(FILE_PICKLE)
    if parsed_Iris_Data == iris_unpickled:
        print('pickling and unpickling successfully done!!')
        print(iris_unpickled)
