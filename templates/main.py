# #nlp
# import functions_framework
# from google.cloud import storage,bigquery,language_v1
#
# #scarping
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import timeit
#
#
# final_data = []
# def print_result(annotations,review):
#     score = annotations.document_sentiment.score
#     magnitude = annotations.document_sentiment.magnitude
#
#     for index, sentence in enumerate(annotations.sentences):
#         sentence_sentiment = sentence.sentiment.score
#         #print(f"Sentence {index} has a sentiment score of {sentence_sentiment}")
#         final_data.append([review,sentence_sentiment])
#
# #    print(f"Overall Sentiment: score of {score} with magnitude of {magnitude}")
#     return 0
#
#
#
#
# def analyze(review):
#     """Run a sentiment analysis request on text"""
#     client = language_v1.LanguageServiceClient()
#
#
#     document = language_v1.Document(
#         content=review, type_=language_v1.Document.Type.PLAIN_TEXT
#     )
#     annotations = client.analyze_sentiment(request={"document": document})
#
#     # Print the results
#     print_result(annotations,review)
#
# def scrape_reviews():
#     starting_time = timeit.default_timer()
#     print("Start time :", starting_time)
#     options = Options()
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless=new')
#     driver = webdriver.Chrome()
#     driver.get(
#         'https://www.tripadvisor.com/Hotel_Review-g297654-d15527910-Reviews-Lemon_Tree_Premier_City_Center_Pune-Pune_Pune_District_Maharashtra.html#REVIEWS')
#     results = driver.find_elements(By.XPATH, "//span[@class='orRIx Ci _a C ']")
#     print("Number of reviews: ", len(results))
#     i = 1
#     for result in results:
#         print("Review: ", i)
#         i += 1
#         print(result.text)
#         print("--------------------------------------------------------------------------------------")
#     # release the resources allocated by Selenium and shut down the browser
#     driver.quit()
#     # more reviewdata
#     print("Ending time :", timeit.default_timer())
#     print("Time difference :", timeit.default_timer() - starting_time)
#     return results
#
# @functions_framework.cloud_event
# def process_data(cloud_event=None,Request=None):
#
#     rows = scrape_reviews()
#
#     for i in rows:
#       analyze(i[-1])
#     for i in final_data:
#         print(i)
#     print("complete")
#     avg = sum([i[-1] for i in final_data])/len(i)
#     print(avg)
#     return avg
#
