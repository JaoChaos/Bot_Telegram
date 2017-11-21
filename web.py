from flask import Flask,request,jsonify,Response
import json
from bson.json_util import loads
from bson.json_util import dumps
from bson import json_util

class attend():
    def attend(message):
        if message="text"
            return jsonify({"status":"OK"})
        else
            return jsonify({"status":"error"})

@app.route("/")
def raiz():
    return jsonify({"status":"OK"})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)
