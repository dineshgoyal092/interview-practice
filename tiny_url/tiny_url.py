from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import uuid

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/tinyurl"
mongo = PyMongo(app)


@app.route("/get_short_url/<url>", methods=["GET"])
def get_url(url):
    result = mongo.db.url.find_one({ "url" : url})
    domain = 'mytiny.domain'
    s = url
    if result:
        s = result['tinyurl']
    else:
        x = uuid.uuid4()
        s = str(x)[:8]
        result = mongo.db.url.find_one({"tinyurl": s})
        while(result):
            x = uuid.uuid4()
            s = str(x)[:8]
            result = mongo.db.url.find_one({"tinyurl": s})
        mongo.db.url.insert({"tinyurl":s,"url":url})
    return "http://{}/{}".format(
        domain,
        s
    )

if __name__ == '__main__':
    app.run(debug=True)