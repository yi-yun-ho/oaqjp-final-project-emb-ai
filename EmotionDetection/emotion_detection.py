
#import necessary modules
import requests
import json

#define app
def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_obj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json = input_obj, headers = headers)
    formatted_response = json.loads(response.text)

    emotion_predicted = formatted_response["emotionPredictions"][0]["emotion"]
    
    max_value = max(emotion_predicted.values())
    dominant_emotion = [key for key, value in emotion_predicted.items() if value == max_value]

    emotion_predicted["dominant_emotion"]=dominant_emotion[0]

    return emotion_predicted

