import time
import requests
from plyer import notification

def NotifyMe(): 
    # url for news api
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=2c68ed861bc640639a38169d158478dc"

    #fetching the news api
    data = requests.get(url=main_url)

    #getting its json file
    Mydata=data.json()

    article = Mydata["articles"]

    for newsitem in article:
        notification.notify(
            title ="HEADLINES : "+ newsitem['source']['name'],
            message =newsitem['title'],
            app_icon = r"C:\Users\user\Desktop\F!Zz@\python\NotifyMe\news.ico",#specify the path of your icon
            timeout= 10,
        )
        time.sleep(2*3600)

if __name__ == '__main__':
    while True:
        NotifyMe()
     