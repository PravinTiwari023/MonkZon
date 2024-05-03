from flask import Flask, render_template, request, jsonify
from LLM import generate_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def receive_message():
    # Get the user message from the request data
    data = request.get_json()
    user_message = data.get('message')

    text = generate_text(user_message)

    # Process the user message (call your logic here)
    # ...

    # Generate a response message from the bot

    # Return the bot message as JSON
    return jsonify({'message': text})

if __name__ == '__main__':
    app.run(debug=True)