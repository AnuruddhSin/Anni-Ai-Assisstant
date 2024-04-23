import pyttsx3
import speech_recognition as sr
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty("rate", 170)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source, 0, 4)

        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query.lower()

    def play_game(self):
        self.speak("Let's play ROCK PAPER SCISSORS!")
        print("LET'S PLAY!")
        i = 0
        me_score = 0
        com_score = 0

        while i < 5:
            choices = ("rock", "paper", "scissors")
            com_choice = random.choice(choices)
            query = self.take_command()

            if query in choices:
                if query == com_choice:
                    self.speak(com_choice.capitalize())
                elif (query == "rock" and com_choice == "scissors") or \
                        (query == "paper" and com_choice == "rock") or \
                        (query == "scissors" and com_choice == "paper"):
                    self.speak(com_choice.capitalize())
                    me_score += 1
                else:
                    self.speak(com_choice.capitalize())
                    com_score += 1

                print(f"Score: ME: {me_score} COM: {com_score}")
                i += 1
            else:
                self.speak("Invalid choice. Please say rock, paper, or scissors.")

        print(f"FINAL SCORE: ME: {me_score} COM: {com_score}")

if __name__ == "__main__":
    rps_game = RockPaperScissorsGame()
    rps_game.play_game()
