from util import Util

util = Util()

dataset = util.load_data('../dataset/iris.data')
print(dataset.groupby('class').size())
