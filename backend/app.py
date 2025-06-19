from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)
app.secret_key = 'secret'

# Load and prepare dataset
df = pd.read_csv('spam.csv')
df.dropna(inplace=True)
df = df[['label', 'message']]
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X = df['message']
y = df['label']

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1234':
        session['user'] = username
        return redirect(url_for('home'))
    else:
        return render_template('login.html', error='Invalid credentials')

@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data['message']
    vector = vectorizer.transform([message])
    prediction = model.predict(vector)
    result = "Spam" if prediction[0] == 1 else "Not Spam"
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
