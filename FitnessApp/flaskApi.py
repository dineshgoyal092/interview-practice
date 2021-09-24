import flask
from flask import Flask, jsonify, abort, make_response
app = flask.Flask(__name__)
app.config["DEBUG"] = True
import requests

@app.route('/health', methods=['GET'])
def health():
    return {"success": True}

if __name__ == "__main__":
    app.run()