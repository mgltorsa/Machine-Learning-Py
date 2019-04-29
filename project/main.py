from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_digits

digits = load_digits()

y = digits["target"]
x = digits["images"]

nb = GaussianNB()
fit  = nb.fit(x[:5],y[:5])

fit.predict(x[:5])