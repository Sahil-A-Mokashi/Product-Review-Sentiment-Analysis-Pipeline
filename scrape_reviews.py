#scarping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from googlesearch import search
import timeit
import sites

def query_generator(p_name,p_cat):
    query=""
    if p_cat=="household":
        query="mouthshut "+p_name+" reviews"
    elif p_cat=="automobile":
        query="carwale "+ p_name + "/user-reviews/"
    elif p_cat=="gadgets":
        query="gadgets360 "+ p_name 
    elif p_cat=="fasion":
        query="trustpilot "+ p_name
    return query

def url_generator(p_name,p_cat):
    for url in search(query_generator(p_name,p_cat), tld="co.in", num=1, stop=1, pause=2):
        print(url)
        print(type(url))
        return url

def scraper(name,category):
    print(name,category)
    print(type(name),type(category))
    if not name: print("no name specified")
    starting_time = timeit.default_timer()
    print("Start time :", starting_time)
    # options = Options()
    options = webdriver.ChromeOptions()
    UserAgent =  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    options.add_argument(f'user-agent={UserAgent}')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    product_url = str(url_generator(name,category))
    print(product_url)
    print(type(product_url))
    # try :
    driver.get(product_url)
    for i in range(len(product_url)):
        if product_url[i:i+4]==".com":
            website_name = product_url[:i+4]
            print(website_name)
            break
    xpath = sites.sites_mapping[website_name]
    print(xpath)
    results = driver.find_elements(By.XPATH, xpath)
    print("Number of reviews: ", len(results))
    i = 1
    res = []
    for result in results:
        # print("Review: ", i)
        i += 1
        #print(result.text)
        res.append(result.text)
        #print("--------------------------------------------------------------------------------------")
    # release the resources allocated by Selenium and shut down the browser
    driver.quit()
    # more reviewdata
    print(len(res))
    print("Ending time :", timeit.default_timer())
    print("Time difference :", timeit.default_timer() - starting_time)
    return res
    # except Exception as e:
    #     print(e)
    