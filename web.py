from flask import Flask,request,jsonify,Response
import json

app = Flask(__name__)
{
   "status": "OK"
}

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
    return jsonify({"status":"OK"})

app.add_resource(attend_info, '/app/attend_info')
app.add_resource(attend_command, '/app/attend_command')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)
