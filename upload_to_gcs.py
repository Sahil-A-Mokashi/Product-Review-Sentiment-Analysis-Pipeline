from google.cloud import storage
#pip install google-cloud-storage
import constant
import uuid
import datetime

def upload(reviews,product_category):
    # reviews  = [str(item).replace(',',' ').replace('\n','') for item in reviews]
    unique_id=str((uuid.uuid1()).int)[:-10][::-1]
    print(unique_id)
    csv_content = ''
    for i,item in enumerate(reviews,start=1):
        try:
            item = str(item).replace('\n','')#.replace('.',' ').replace(','," ")
            # csv_content+=f'{i},{item}\n'
            csv_content+=f'{item}\n'
            print(item)
        except Exception as e:
            print("error converting the data to string while creating the txt")
    client = storage.Client()
    bucket = client.get_bucket(constant.bucket)
    csv_content.encode('utf-8')
    blobname=str(f"semicolons/reviews_{product_category}/")+str(unique_id)+"_reviews_"+str(product_category)+str(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f'))+".txt"
    blob = bucket.blob(blobname)
    try:
        blob.upload_from_string(csv_content,content_type='text/csv')
        print(f"upload successfull to : gs://{constant.bucket}/{blobname}")
        return {"value":200,"message":"successfully uploaded","blobname":f"{blobname}"}
    except Exception as e:
        print(f"error uploading to gcs : {e}")
        return {"value":500,"message":f"error uploading to gcs : {e}","blobname":None}