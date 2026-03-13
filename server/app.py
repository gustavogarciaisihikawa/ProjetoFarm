from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for computers
computers = {}

@app.route('/register', methods=['POST'])
def register_computer():
    data = request.json
    computer_id = data.get('id')
    if not computer_id:
        return jsonify({'error': 'Computer ID is required.'}), 400
    computers[computer_id] = {'status': 'registered'}
    return jsonify({'message': 'Computer registered successfully.'}), 201

@app.route('/heartbeat/<computer_id>', methods=['POST'])
def heartbeat(computer_id):
    if computer_id not in computers:
        return jsonify({'error': 'Computer not registered.'}), 404
    computers[computer_id]['status'] = 'alive'
    return jsonify({'message': 'Heartbeat received.'}), 200

@app.route('/command', methods=['POST'])
def manage_command():
    data = request.json
    command = data.get('command')
    computer_id = data.get('id')
    if not command or not computer_id:
        return jsonify({'error': 'Command and Computer ID are required.'}), 400
    if computer_id not in computers:
        return jsonify({'error': 'Computer not registered.'}), 404
    # Here you'd have logic to send command to computer
    return jsonify({'message': f'Command sent to {computer_id}'}), 200

if __name__ == '__main__':
    app.run(debug=True)