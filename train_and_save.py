# train_and_save.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1) Load a sample (5000 rows)
df = pd.read_csv("malicious_phish.csv").sample(n=5000, random_state=42)

# 2) Encode labels
encoder = LabelEncoder()
df['type'] = encoder.fit_transform(df['type'])

# 3) TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['url'])
y = df['type']

# 4) Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_jobs=-1, random_state=42)
model.fit(X_train, y_train)

# 5) Evaluate (optional)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=encoder.classes_))

# 6) Save artifacts
joblib.dump(model, "rf_model.joblib")
joblib.dump(vectorizer, "tfidf_vectorizer.joblib")
joblib.dump(encoder, "label_encoder.joblib")
print("Saved model, vectorizer and encoder.")
