from flask import Flask, jsonify, request
app = Flask(__name__)
hearts = [
{
    "heart_id": "1",
    "date": "November 29",
    "heart_rate": "110/60"
}
]

@app.route('/hearts', methods = ['Get'])
def getHearts():
    return jsonify(hearts)
    
@app.route('/hearts', methods=['POST'])
def add_heart():
    heart = request.get_json()
    hearts.append(heart)
    return {'id': len(hearts)}, 200

@app.route('/hearts/<int:index>', methods=['DELETE'])
def delete_heart(index):
    hearts.pop(index)
    return 'The heart has been deleted', 200

if __name__ == '__main__':
    app.run()