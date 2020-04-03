from flask import *
from flask_pymongo import PyMongo

app = Flask('Note Manager')
app.config['MONGO_URI'] = "mongodb://localhost:27017/note-manager-db"

mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        pass


app.run(debug=True)


