
from flask import Flask
import os
import json
from flask import Flask,request,jsonify,Response
from bson import json_util

def attend(message):
    if message="text"
        return jsonify({"status":"OK"})
    else
        return jsonify({"status":"error"})

@app.route("/")
def raiz():
    data = {"status": "OK"}
    return json.dumps(data)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)
