import google.generativeai as palm 
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('API_KEY')

palm.configure(api_key=API_KEY)

def text_generation(overall_sentiment_score):
    completion = palm.generate_text(
    model='models/text-bison-001',
    prompt = f"There is a usecase of sentiment analysis based on reviews, the sentiment score ranges between -1.0 and 1.0 where more the negative worse the product is and more positive the score is more better the product is. Please generate a 6-7 lines or 200 word summary about the product based on the sentiment score. The sentiment score is {overall_sentiment_score}, do not mention the score anywhere",
    temperature=0.8,
    max_output_tokens=800,
    )
    output=str(completion.result)
    print("*********************************")
    print(output)
    print("*********************************")
    return output