import wolframalpha
import pyttsx3
import speech_recognition

class Assistant:
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[0].id)
        self.engine.setProperty("rate", 170)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def wolf_ram_alpha(self, query):
        apikey = "JX4K85-334Q87HQWT"
        requester = wolframalpha.Client(apikey)
        requested = requester.query(query)

        try:
            answer = next(requested.results).text
            return answer
        except:
            self.speak("The value is not answerable")

    def calc(self, query):
        term = str(query)
        term = term.replace("anni", "")
        term = term.replace("multiply", "*")
        term = term.replace("plus", "+")
        term = term.replace("minus", "-")
        term = term.replace("divide", "/")

        final = str(term)
        try:
            result = self.wolf_ram_alpha(final)
            print(f"{result}")
            self.speak(result)
        except:
            self.speak("The value is not answerable")
