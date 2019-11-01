from warnings import simplefilter
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from util import Util

simplefilter(action='ignore', category=FutureWarning)

util = Util()
dataset = util.load_data('../dataset/iris.data')

# separacao dos dados
array = dataset.values
x = array[:,0:4]
y = array[:,4]
validation_size = 0.1
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(x, y, test_size=validation_size, random_state=seed)


# definicao dos algoritoms que serao executados
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# avaliacao dos resultados
results = []
names = []
for name, model in models:
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f " % (name, cv_results.mean())
    print(msg)
