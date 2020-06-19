from flask import *
from flask_pymongo import PyMongo
from pymongo import MongoClient
import random

app = Flask("Jumbled Words")
app.config["MONGO_URI"] = "mongodb://localhost:27017/jumbled-words-db"

mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        documents = mongo.db.wordcollection.find()
        return render_template('index.html')


@app.route('/jumble', methods=['GET', 'POST'])
def jumble():
    if request.method == 'GET':
        return render_template('jumble.html')

    elif request.method == 'POST':
        word = request.form.get('entry')
        print(word)
        words = {'word': word}
        mongo.db.wordcollection.insert_one(words)
        return redirect('/database')


@app.route('/jumble2', methods=['GET', 'POST'])
def jumble2():
    if request.method == 'GET':
        return render_template('jumble2.html')

    elif request.method == 'POST':
        word = request.form.get('entry')
        print(word)
        words = {'word': word}

        client = MongoClient("mongodb://127.0.0.1:27017")
        db = client['jumbled-words-db']
        col = db['wordcollection']
        col.insert(words)

        return redirect('/database')


@app.route('/figureout', methods=['GET', 'POST'])
def figureout():
    if request.method == 'GET':
        documents = mongo.db.wordcollection.find()
        words = []
        for obj in documents:
            word = list(obj['word'])
            random.shuffle(word)
            words.append(word)
        return render_template('figureout.html', results=words)

    elif request.method == 'POST':
        pass


@app.route('/database', methods=['GET'])
def database():
    if request.method == 'GET':
        client = MongoClient("mongodb://127.0.0.1:27017")
        with client:
            dblist = client.list_database_names()

        documents = mongo.db.wordcollection.find()
        return render_template('database.html', results=documents, databases=dblist)


app.run(debug=True)