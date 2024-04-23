import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

class Searching_Area:
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[0].id)
        self.engine.setProperty("rate", 170)

    def takeCommand(self):
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source, 0, 4)
        try:
            print("Understanding..")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query.lower()

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def searchGoogle(self, query):
        if "google" in query:
            query = query.replace("anni", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            self.speak("This is what I found on google")
            try:
                pywhatkit.search(query)
                result = wikipedia.summary(query, 1)
                self.speak(result)
            except:
                self.speak("No speakable output available")

    def searchYoutube(self, query):
        if "youtube" in query:
            self.speak("This is what I found for your search!")
            query = query.replace("youtube search", "")
            query = query.replace("youtube", "")
            query = query.replace("anni", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            self.speak("Done, Sir")

    def searchWikipedia(self, query):
        if "wikipedia" in query:
            self.speak("Searching from Wikipedia....")
            query = query.replace("wikipedia", "")
            query = query.replace("search wikipedia", "")
            query = query.replace("anni", "")
            results = wikipedia.summary(query, sentences=2)
            self.speak("According to Wikipedia..")
            print(results)
            self.speak(results)

