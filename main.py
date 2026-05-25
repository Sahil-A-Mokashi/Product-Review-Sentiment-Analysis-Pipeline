from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import constant

#custom methods
import scrape_reviews as sr
import upload_to_gcs
import authenticated_session
import gen_ai_text_generation   

app = Flask(__name__)

formdata = {}

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        product_name = request.form['pname']
        formdata['product_name'] = product_name
        temp = str(product_name + '"')
        # product_url = request.form['purl']
        # formdata['product_url'] = product_url

        product_category = request.form['category']
        formdata['category'] = product_category


        reviews = sr.scraper(str(product_name),str(product_category))
        if not reviews:
            print("no reviews scraped , ending process")
            return "no reviews scraped"
        uploader = upload_to_gcs.upload(reviews,product_category)
        if uploader['blobname']:
            blobname = uploader['blobname']


        # params = {'bucket_name':constant.bucket,'filename':constant.blobname}
        # session = authenticated_session.get_my_session() if authenticated_session.get_my_session() else requests
        # response = session.post(str(f"https://us-central1-poc-analytics-ai.cloudfunctions.net/sentiment-analysis"),params=params)
        # print(response)
        # return str(response)

        url = "https://us-central1-poc-analytics-ai.cloudfunctions.net/sentiment-analysis-public"

        payload = json.dumps({
            "blobname": f"{blobname}",
            "bucketname":f"{constant.bucket}"
        })
        token = authenticated_session.get_access_token()
        headers = {
            'Authorization': f'bearer {token}',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        print(response.text)
        print(type(response.text))
        # result = json.loads(response.text)
        # show_data = {"sentiment score":result['result ']['overall_sentiment_score'],
        #              }
        result =  json.loads(response.text)
        # result =  json.loads(result['overall_sentiment_score'])
        print(result)
        # print(type(result))
        # print(result['dictionary'])
        # print(type(result['dictionary']))
        overall_sentiment_score = result['result ']['overall_sentiment_score']
        overall_sentiment_score_percentage = ((overall_sentiment_score+1)/2 ) * 100
        sentiment_reviews_pairs=[]
        for i in result['result ']['sentences']:
            score=i[0]
            review=i[2]
            sentiment_reviews_pairs.append([score,review])

        sentiment_llm_response = gen_ai_text_generation.text_generation(overall_sentiment_score) #todo: for @akshay add the llm call here, return string to this variable
        print("-----------------------------")
        print(sentiment_llm_response)
        print("-----------------------------")
        return render_template('output.html',overall_sentiment_score_percentage = overall_sentiment_score_percentage,sentiment_llm_response=sentiment_llm_response)
        # return result
        # print(json.loads(result["result"]))
        # return show_data
        #return redirect(f"https://{constant.cloud_function_region}-{constant.project_id}.cloudfunctions.net/{constant.cloud_function_name}?product_name=" + temp)
    else:
        return render_template('home.html')

@app.route('/output')
def output():
    return render_template('output.html',overall_sentiment_score = 69,sentiment_llm_response="kuch toh product do bhai")

if __name__ == '__main__':
    app.run(debug=True,port=8080)
