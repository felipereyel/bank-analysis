from util import Util
import matplotlib.pyplot as plt

util = Util()

dataset = util.load_data('../dataset/iris.data')
dataset.plot(kind='box', subplots=True, sharex=False, sharey=False)
plt.show()
