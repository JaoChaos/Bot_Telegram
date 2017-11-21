from flask import Flask,request,jsonify,Response
import json
from bson.json_util import loads
from bson.json_util import dumps
from bson import json_util

class attend():
    def attend_info(message):
        return jsonify({"status":"OK"})

    def attend_command(message):
        return jsonify({"status":"OK"})

@app.route("/")
def raiz():
    return jsonify({"status":"OK"})

api.add_resource(attend_info, '/api/attend_info')
api.add_resource(attend_command, '/api/attend_command')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)
