def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    print(str)
    speak.Speak(str)

def fetch_news(time_date):
    import requests
    api_news = {"X-Api-Key": "4413ce6f56c64add9737cf93292abdcd"}
    news_selecting_param = {"country": "in", "from": time_date, "Source": "TimesOfIndia"}

    news_request = requests.get("https://newsapi.org/v2/top-headlines", headers=api_news,params=news_selecting_param)

    return news_request

def news_processing(news_request):
    import json

    news = news_request.text
    news = json.loads(news)
    news = news['articles']

    news_filtered = list(filter(lambda x:x['description'] is not None, news[0:len(news)]))
    return news_filtered

if __name__ == '__main__':
    from datetime import datetime

    time_date = datetime.now()
    time_now = time_date.strftime("%H:%M:%S")


    numbering = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'last'}

    greeting = ""
    end_greetings = ""
    if int(time_now.split(":")[0]) >= 18:
        greeting = "Evening"
        end_greetings = "Good night, sleep tight"
    elif int(time_now.split(":")[0]) >= 12:
        greeting = "Afternoon"
        end_greetings = "Have a wonderful afternoon"
    else:
        greeting = "Morning"
        end_greetings = "Have a nice day"

    def With_Greetings(news):
        def Apply_Greetings(news_filtered):
            speak(f"Good {greeting} user\n Here's your timely news content")
            news(news_filtered)
            speak(end_greetings)
        return Apply_Greetings

    @With_Greetings
    def Speak_input(news_filtered):
        for i in range(10):
            speak(f"{numbering[i+1]} headline \n"+news_filtered[i]['description'])


    Speak_input(news_processing(fetch_news(time_date)))
    while True:
        time_date = datetime.now()
        time_now = time_date.strftime("%H:%M:%S")

        if time_now == "18:00:00":
            Speak_input(news_processing(fetch_news(time_date)))
        elif time_now == "12:00:00":
            Speak_input(news_processing(fetch_news(time_date)))
        elif time_now == "00:00:00":
            Speak_input(news_processing(fetch_news(time_date)))


