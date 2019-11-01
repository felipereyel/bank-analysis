import pandas


class Util:

    def load_data(self, file_name):
        url = file_name
        names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
        dataset = pandas.read_csv(url, names=names)
        return dataset
