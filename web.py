from flask import Flask,request,jsonify,Response
import json

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

def raiz():
    return jsonify({"status":"OK"})

api.add_resource(attend_info, '/api/attend_info')
api.add_resource(attend_command, '/api/attend_command')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)
