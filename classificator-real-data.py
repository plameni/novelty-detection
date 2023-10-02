from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
import numpy as np
from sklearn.datasets import load_files
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import scikitplot as skplt
import time
from sklearn.metrics import PrecisionRecallDisplay

categories = ['allowed', 'forbidden']
# data = load_files('no-processing', categories=categories, shuffle=True, random_state=0)

# data = load_files('./new-test/classify-no-processing', categories=categories, random_state=42)
start_time = time.time()
data = load_files('./new-test/28th-preprocessed', categories=categories, random_state=42)
print(data.target_names)

X_train, X_test, Y_train, Y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42) 

"""
classifier = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
])

"""
classifier = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
                                          alpha=1e-3, random_state=42)),
])


classifier = classifier.fit(X_train, Y_train)

predicted = classifier.predict(X_test)
print("--- %s seconds ---" % (time.time() - start_time))
result = np.mean(predicted == Y_test)
print(result)

y_score = classifier.decision_function(X_test)

"""
display = PrecisionRecallDisplay.from_estimator(Y_test, y_score, name="LinearSVC")
display.ax_.set_title("2-class Precision-Recall curve")
"""

fig = plt.figure(figsize=(15,6))

ax1 = fig.add_subplot(121)
skplt.metrics.plot_confusion_matrix(Y_test, predicted,
                                    title="Confusion Matrix",
                                    #cmap="Oranges",
                                    ax=ax1)


