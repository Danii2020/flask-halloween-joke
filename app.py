from flask import Flask, jsonify
import pyttsx3

app = Flask(__name__)

engine = pyttsx3.init()
engine.setProperty('rate', 145)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[21].id)
# for index, voice in enumerate(voices):
#     print(f"Index {index} {voice.languages}")

def speak(text):
    engine.say(text)
    engine.runAndWait()
    if engine._inLoop:
        engine.endLoop()

@app.route("/speak/<string:message>", methods=["GET"])
def speak_message(message):
    try:
        speak(message)
        return jsonify({"message": "Message spoke successfully!"}), 200
    except Exception as e:
        return jsonify({"message": f"There was an error: {e}"}), 500
    
if __name__ == '__main__':
    app.run(host="192.168.100.40", debug=True) # replace host with your actual IP