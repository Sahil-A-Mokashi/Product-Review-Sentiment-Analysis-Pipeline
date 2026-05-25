response = {
  "documentSentiment": {
    "score": 0.2,
    "magnitude": 3.6
  },
  "language_code": "en",
   "sentences": [
    {
      "text": {
        "content": """Four score and seven years ago our fathers brought forth
        on this continent a new nation, conceived in liberty and dedicated to
        the proposition that all men are created equal.""" ,
        "beginOffset": 0
      },
      "sentiment": {
        "magnitude": 0.8,
        "score": 0.8
      }
    },
{
      "text": {
        "content": """Four score and seven years ago our fathers brought forth
        on this continent a new nation, conceived in liberty and dedicated to
        the proposition that all men are created equal.""",
        "beginOffset": 0
      },
      "sentiment": {
        "magnitude": 0.8,
        "score": 0.8
      }
    },
   ]
}

import json
dictionary = {}
dictionary['overall_sentiment_score'] = response['documentSentiment']['score']
dictionary['overall_magnitude_score'] = response['documentSentiment']['magnitude']
dictionary['sentences']=[]
# dictionary['sentences'] = {[response]['sentences']['text'] : [response]['sentences']['sentiment']['score'] for response['sentences'] in response['sentences']}
for i in response['sentences']:
    dictionary['sentences'].append([i['sentiment']['score'],i['sentiment']['magnitude'],i['text']['content']])
    print(i['text']['content'],i['sentiment']['score'],i['sentiment']['magnitude'])
print(dictionary)
json_string = json.dumps(dictionary)
print(json_string)






