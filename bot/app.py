from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample responses
responses = {
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a computer program, but I'm doing well. How can I assist you?",
    "bye": "Goodbye! Have a great day.",
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower()
    bot_response = responses.get(user_message, "I'm not sure how to respond to that.")
    return jsonify({"message": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
