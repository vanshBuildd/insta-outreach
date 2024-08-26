from flask import Flask, request, jsonify
import os
from selenium_script import send_instagram_message  # Correct import

app = Flask(__name__)


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    receiver_username = data.get('receiver_username')

    if not receiver_username:
        return jsonify({"error": "receiver_username is required"}), 400

    try:
        send_instagram_message(receiver_username)
        return jsonify({"status": "Message sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', '8080'))
