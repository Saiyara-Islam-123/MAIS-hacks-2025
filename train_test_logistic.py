from sklearn.linear_model import LogisticRegression
from dataset import get_test_train
import pickle

logisticRegr = LogisticRegression(max_iter=10000)
X_train, y_train, X_test, y_test = get_test_train()

logisticRegr.fit(X_train, y_train)

score = logisticRegr.score(X_test, y_test)
print(score * 100)

with open('trained_model.pkl', 'wb') as f:
    pickle.dump(logisticRegr, f)