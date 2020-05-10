from flask import *
from flask_pymongo import PyMongo
from pymongo import MongoClient


app = Flask('Jumbled Words')
app.config['MONGO_URI'] = "mongodb://localhost:27017/jumbled-words-db"


mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    client = MongoClient("mongodb://127.0.0.1:27017")

    with client:
        dblist = client.list_database_names()

    if request.method == 'GET':
        documents = mongo.db.wordcollection.find()
        return render_template('index.html', databases=dblist)

    elif request.method == 'POST':
        word = request.form.get('entry')
        print(word)
        words = {'word': word}
        mongo.db.wordcollection.insert_one(words)
        return redirect('/')


@app.route('/figureout', methods=['GET', 'POST'])
def figureout():
    if request.method == 'GET':
        documents = mongo.db.wordcollection.find()
        return render_template('figureout.html', results=documents)

    elif request.method == 'POST':
        pass


app.run(debug=True)
