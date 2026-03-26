from EmotionDetection.emotion_detection import emotion_detector

def emotion_detector_function(text_to_analyze):
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None
        }

    result = emotion_detector(text_to_analyze)

    return {
        "anger": result["anger"],
        "disgust": result["disgust"],
        "fear": result["fear"],
        "joy": result["joy"],
        "sadness": result["sadness"]
    }
