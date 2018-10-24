import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version = '2016-05-19',
    username = 'd28010de-72f9-4a46-b074-b401c051e339',
    password = 'P6NvqK1kqxU6',
    url = 'https://gateway.watsonplatform.net/tone-analyzer/api'
)

def get_tone(text):
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json').get_result()
    emotions = tone_analysis["document_tone"]["tone_categories"]
    mood_dict = {
        "anger" : emotions[0]["tones"][0]["score"],
        "disgust" : emotions[0]["tones"][1]["score"],
        "fear" : emotions[0]["tones"][2]["score"],
        "joy" : emotions[0]["tones"][3]["score"],
        "sadness" : emotions[0]["tones"][4]["score"],
        "analytical" : emotions[1]["tones"][0]["score"],
        "confident" : emotions[1]["tones"][1]["score"],
        "tentative" : emotions[1]["tones"][2]["score"],
        "openness" : emotions[2]["tones"][0]["score"],
        "conscientiousness" : emotions[2]["tones"][1]["score"],
        "extraversion" : emotions[2]["tones"][2]["score"],
        "agreeableness" : emotions[2]["tones"][3]["score"],
        "emotional range" : emotions[2]["tones"][4]["score"]
    }
    return mood_dict

text = 'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'
