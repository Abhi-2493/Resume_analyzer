from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = [
    ("python machine learning data analysis", "Data Science"),
    ("html css javascript frontend backend", "Web Development"),
    ("java spring sql", "Java Developer"),
    ("cloud aws gcp devops", "Cloud Engineer"),
]

texts, labels = zip(*data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

def predict_domain(text):
    X_test = vectorizer.transform([text])
    return model.predict(X_test)[0]
