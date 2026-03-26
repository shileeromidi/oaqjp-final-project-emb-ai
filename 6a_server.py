from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    This endpoint takes text as input and returns emotion analysis.
    Example usage:
    http://localhost:5000/emotionDetector?text=I am happy
    """
    text_to_analyze = request.args.get('text')

    if not text_to_analyze:
        return jsonify({"error": "Invalid input! Please enter some text to analyze."}), 400

    result = emotion_detector(text_to_analyze)

    if result is None or result['dominant_emotion'] is None:
        return jsonify({"error": "Could not process the request."}), 500

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
