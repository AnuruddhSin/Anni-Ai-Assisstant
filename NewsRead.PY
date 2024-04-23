import requests
import json
import pyttsx3
import speech_recognition


class NewsReader:
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[0].id)
        self.engine.setProperty("rate", 170)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()



    def latest_news(self):
        api_dict = {
            "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=ebb55c6ae65a4aedb1a176b9c7ee604a",
            "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=ebb55c6ae65a4aedb1a176b9c7ee604a",
            "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=ebb55c6ae65a4aedb1a176b9c7ee604a",
            "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=ebb55c6ae65a4aedb1a176b9c7ee604a",
            "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=ebb55c6ae65a4aedb1a176b9c7ee604a",
            "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=ebb55c6ae65a4aedb1a176b9c7ee604a"
        }

        content = None
        url = None
        self.speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
        field = input("Type field news that you want: ")
        for key, value in api_dict.items():
            if key.lower() in field.lower():
                url = value
                print(url)
                print("url was found")
                break
            else:
                url = True
        if url is True:
            print("url not found")

        news = requests.get(url).text
        news = json.loads(news)
        self.speak("Here is the first news.")

        arts = news["articles"]
        for articles in arts:
            article = articles["title"]
            print(article)
            self.speak(article)
            news_url = articles["url"]
            print(f"For more info visit: {news_url}")

            a = input("[press 1 to continue] and [press 2 to stop]")
            a = self.take_command()
            if str(a) == "1":
                pass
            elif str(a) == "2":
                break

        self.speak("That's all")

    def take_command(self):
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source, 0, 4)

        try:
            print("Understanding.... ")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query

# if __name__ == "__main__":
#     news_reader = NewsReader()
#     news_reader.latest_news()
