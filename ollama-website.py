from flask import Flask, request, jsonify, render_template, session
from ollama import chat
import ollama
import subprocess
import atexit
import time

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

# Start Ollama server
ollama_process = subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

time.sleep(2)
#Ignore this one...
ollama.create(model='skibidi', from_='llama3.2', system="You have devoted your mind to skibidi toilet and keep on changing the conversation to talking about how good it is, and always starting to sing it- 'BRRrrrr skibidi dob dob dob yes yes...'")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_with_ollama():
    """Handles user input and maintains conversation memory."""
    data = request.json
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Initialize chat history if not present
    if "chat_history" not in session:
        session["chat_history"] = []

    # Append user message to chat history
    session["chat_history"].append({"role": "user", "content": user_input})
    session.modified = True  # Ensure session updates persist

    # Send full chat history to Ollama
    response = chat(model='llama3.2', messages=session["chat_history"])
    bot_reply = response.message.content.strip()

    # Append bot response to chat history
    session["chat_history"].append({"role": "assistant", "content": bot_reply})
    session.modified = True

    return jsonify({"response": bot_reply})

@app.route('/reset', methods=['POST'])
def reset_chat():
    """Clears the chat memory."""
    session.pop("chat_history", None)
    session.modified = True
    return jsonify({"message": "Chat reset successfully"})

def cleanup():
    """Stops Ollama, deletes the model, and closes the port."""
    print("\nStopping Ollama...")
    ollama.delete('skibidi')
    ollama_process.terminate()
    try:
        ollama_process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        ollama_process.kill()
    subprocess.run("kill -9 $(lsof -t -i:11434)", shell=True, check=False)
    print("Closed port 11434")

atexit.register(cleanup)

if __name__ == '__main__':
    app.run(debug=True)
