from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import datetime

def task3(features, target):
    count_vec = CountVectorizer()
    count_vecd_features = count_vec.fit_transform(features)
    X_train, X_test, y_train, y_test = train_test_split(count_vecd_features, target, test_size=0.25, random_state=101)
    try:
        classifier = joblib.load('C:\\Users\\Dan Siegel\\Desktop\\Classes\\550\\final\\models\\model.pkl')
    except:
        classifier = LogisticRegression(penalty='l1')
    mod = classifier.fit(X_train, y_train)
    test_pred = mod.predict(X_test)
    accuracy_test = accuracy_score(y_test, test_pred)
    now = datetime.datetime.now()
    joblib.dump(mod, 'C:\\Users\\Dan Siegel\\Desktop\\Classes\\550\\final\\models\\model.pkl') 
    with open('C:\\Users\\Dan Siegel\\Desktop\\Classes\\550\\final\\reports\\report1.md', 'a+') as mdWriter:
        mdWriter.writelines(('Regression run at:', str(now),' accuracy:', str(accuracy_test),'\n'))