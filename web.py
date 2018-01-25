from flask import Flask,request,jsonify,Response
import json
import os

app = Flask(__name__)
{
   "status": "OK"
}
"""
{
   "status": "OK",
   "ejemplo": { "ruta": "/ruta/parametro",
                "valor": "{JSON: devuelto}"
              }
}
"""


@app.route("/status")
def status():
	data = {"status": "OK"}
return json.dumps(data)

class attend():
    def attend_info(message):
        try:
            val = int(message)
            return jsonify({"status":"OK"})
        except ValueError:
            print("That's not an int!")

    def attend_command(message):
        try:
            isinstance(message, str)
            return jsonify({"status":"OK"})
        except ValueError:
            print("Thats not a command!")

@app.route("/")
def raiz():
    data = {"status": "OK"}
    return json.dumps(data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)
