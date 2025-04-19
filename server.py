from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/emotionDetector")
def detector():
    task_to_analyze = request.args.get("textToAnalyze")

    results = emotion_detector(task_to_analyze)

    result_string=f"For the given statement, the system response is 'anger': {results['anger']}, 'disgust': {results['disgust']}, \
    'fear': {results['fear']}, 'joy': {results['joy']} and 'sadness': {results['sadness']}. The dominant emotion is \
     <b>{results['dominant_emotion']}</b>."

    return result_string



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)