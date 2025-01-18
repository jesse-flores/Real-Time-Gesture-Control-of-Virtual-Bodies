from flask import Flask, jsonify, request

app = Flask(__name__)

##Default state
cube_state = {
    "rotation": {"x": 0, "y": 0, "z": 0},
    "translation": {"x": 0, "y": 0, "z": 0},
    "scaling": {"x": 1, "y": 1, "z": 1}
}

@app.route('/get_state')
def get_state():
    return jsonify(cube_state)

@app.route('/update_state', methods=['POST'])
def update_state():
    global cube_state
    cube_state = request.get_json()
    return jsonify({"status": "success", "new_state": cube_state})

if __name__ == '__main__':
    app.run(debug=True)