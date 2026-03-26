from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detection App Running"

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text = request.args.get("textToAnalyze")

    result = emotion_detector(text)

    return (
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, "
        f"joy: {result['joy']}, "
        f"sadness: {result['sadness']}"
    )

if __name__ == "__main__":
    app.run(debug=True)
