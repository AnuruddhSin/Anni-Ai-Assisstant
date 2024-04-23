import sys
import pyttsx3
import speech_recognition
import speedtest
import os
import datetime
import mixer
import langid

# UX designer concept import logic here
from PyQt5 import QtWidgets , QtCore , QtGui
from PyQt5.QtCore import QTimer , QTime , QDate , Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from gui_anni import Ui_MainWindow
from normal_talk import ResponseManager

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

# from INTRO import play_gif
# play_gif


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        self.response_manager = response_manager

    def run(self):
        self.taskExecution()

    # for i in range(3):
    #     a = input("Enter Password to open Anni :- ")
    #     pw_file = open("password.txt", "r")
    #     pw = pw_file.read()
    #     pw_file.close()
    #     if (a == pw):
    #         print("WELCOME Sir Please Speak Paskey for Activate Anni")
    #         break
    #     elif (i == 2 and a != pw):
    #         exit()
    #
    #     elif (a != pw):
    #         print("Try Again")

    def speak(self,audio):
        engine.say(audio)
        engine.runAndWait()

    def takeCommand(self):
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

    def alarm(self,query):
        from al import AlarmApp
        timehere = open("Alarmtext.txt", "a")
        timehere.write(query)
        timehere.close()
        app = AlarmApp()
        os.startfile('al.py')


    def taskExecution(self):
        # if __name__ == "__main__":
        global requests, BeautifulSoup
        while True:
                query = self.takeCommand().lower()
                if "wake up" in query:
                    from GreetMe import greetMe
                    greetMe()

                    while True:
                        query = self.takeCommand().lower()
                        response = self.response_manager.get_response(query)
                        self.speak(response)
                        if "go to sleep" in query:
                            self.speak("Ok sir , You can me call anytime")

                        elif "change password" in query:
                            self.speak("What's the new password")
                            new_pw = input("Enter the new password\n")
                            new_password = open("password.txt", "w")
                            new_password.write(new_pw)
                            new_password.close()
                            self.speak("Done sir")
                            self.speak(f"Your new password is{new_pw}")



                        # elif "hello anni" in query:
                        #     self.speak("Hello sir, how are you ?")
                        # elif "i am fine"  in query:
                        #     self.speak("that's great, sir")
                        # elif "how are you"  in query:
                        #     self.speak("Perfect, sir")
                        # elif "thank you" in query:
                        #     self.speak("you are welcome, sir")

                        elif "pause" in query:
                            pyautogui.press("k")
                            self.speak("video paused")
                        elif "play" in query:
                            pyautogui.press("k")
                            self.speak("video played")
                        elif "mute" in query:
                            pyautogui.press("m")
                            self.speak("video muted")

                        elif "volume up" in query:
                            from keyboard import volumeup

                            self.speak("Turning volume up,sir")
                            volumeup()

                        elif "remember that" in query:
                            rememberMessage = query.replace("remember that", "")
                            rememberMessage = query.replace("anni", "")
                            self.speak("You told me to remember that" + rememberMessage)
                            remember = open("Remember.txt", "a")
                            remember.write(rememberMessage)
                            remember.close()
                        elif "what do you remember" in query:
                            remember = open("Remember.txt", "r")
                            self.speak("You told me to remember that" + remember.read())

                        # elif "tired" in query:
                        #     speak("Playing your favourite songs, sir")
                        #     a = (1, 2, 3)  # You can choose any number of songs (I have only choosen 3)
                        #     b = random.choice(a)
                        #     if b == 1:
                        #         webbrowser.open(" ")

                        elif "news" in query:
                            from NewsRead import NewsReader
                            reader = NewsReader()
                            reader.latest_news()

                        elif "volume down" in query:
                            from keyboard import volumedown

                            self.speak("Turning volume down, sir")
                            volumedown()

                        elif "open" in query:
                            from Dictapp  import openappweb
                            openappweb(query)

                        elif "close" in query:
                            from Dictapp import closeappweb

                            closeappweb(query)

                        elif "google" in query:
                            from SearchNow import Searching_Area

                            assistant = Searching_Area()
                            query = assistant.takeCommand()
                            assistant.searchGoogle(query)
                            assistant.searchYoutube(query)
                            assistant.searchWikipedia(query)
                        elif "youtube" in query:
                            from SearchNow import searchYoutube

                            searchYoutube(query)
                        elif "wikipedia" in query:
                            from SearchNow import searchWikipedia

                            searchWikipedia(query)


                        elif "temperature" in query:
                            search = "temperature in Lucknow"
                            url = f"https://www.google.com/search?q={search}"
                            r = requests.get(url)
                            data = BeautifulSoup(r.text, "html.parser")
                            temp = data.find("div", class_="BNeawe").text
                            self.speak(f"current{search} is {temp}")

                        elif "set an alarm" in query:
                            self.speak("Set the time")
                            from al import AlarmApp
                            ALARAM_APP = AlarmApp()

                            self.alarm(a)

                        elif "calculate" in query:
                            from Calculatenumbers import Assistant
                            assistant = Assistant()
                            query = query.replace("calculate", "")
                            query = query.replace("anni", "")
                            assistant.calc(query)

                            # from Calculatenumbers import Calculator_Assistant
                            # assistant = Calculator_Assistant()
                            #
                            # query = query.replace("calculate", "")
                            # query = query.replace("anni", "")
                            # assistant(query)

                        elif "weather" in query:
                            search = "temperature in Lucknow"
                            url = f"https://www.google.com/search?q={search}"
                            r = requests.get(url)
                            data = BeautifulSoup(r.text, "html.parser")
                            temp = data.find("div", class_="BNeawe").text
                            self.speak(f"current{search} is {temp}")

                        elif "whatsapp" in query:
                            from Whatsapp import sendMessage
                            sendMessage()

                        elif "schedule my day" in query:
                            tasks = []  # Empty list
                            self.speak("Do you want to clear old tasks (Plz speak YES or NO)")
                            query = self.takeCommand().lower()
                            if "yes" in query:
                                file = open("tasks.txt", "w")
                                file.write(f"")
                                file.close()
                                no_tasks = int(input("Enter the no. of tasks :- "))
                                i = 0
                                for i in range(no_tasks):
                                    tasks.append(input("Enter the task :- "))
                                    file = open("tasks.txt", "a")
                                    file.write(f"{i}. {tasks[i]}\n")
                                    file.close()
                            elif "no" in query:
                                i = 0
                                no_tasks = int(input("Enter the no. of tasks :- "))
                                for i in range(no_tasks):
                                    tasks.append(input("Enter the task :- "))
                                    file = open("tasks.txt", "a")
                                    file.write(f"{i}. {tasks[i]}\n")
                                    file.close()

                        elif "show my schedule" in query:
                            file = open("tasks.txt", "r")
                            content = file.read()
                            file.close()
                            mixer.init()
                            mixer.music.load("notification.mp3")
                            mixer.music.play()
                            notification.notify(
                                title="My schedule :-",
                                message=content,
                                timeout=15
                            )

                        # elif "open" in query:  # EASY METHOD
                        #     query = query.replace("open", "")
                        #     query = query.replace("anni", "")
                        #     pyautogui.press("super")
                        #     pyautogui.typewrite(query)
                        #     pyautogui.sleep(2)
                        #     pyautogui.press("enter")

                        elif "internet speed" in query:
                            wifi = speedtest.Speedtest()
                            upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
                            download_net = wifi.download() / 1048576
                            print("Wifi Upload Speed is", upload_net)
                            print("Wifi download speed is ", download_net)
                            self.speak(f"Wifi download speed is {download_net}")
                            self.speak(f"Wifi Upload speed is {upload_net}")

                        elif "ipl score" in query:
                            from plyer import notification
                            import requests
                            from bs4 import BeautifulSoup

                            url = "https://www.cricbuzz.com/"
                            page = requests.get(url)
                            soup = BeautifulSoup(page.text, "html.parser")
                            team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                            team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                            team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
                            team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

                            a = print(f"{team1} : {team1_score}")
                            b = print(f"{team2} : {team2_score}")

                            notification.notify(
                                title="IPL SCORE :- ",
                                message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                                timeout=15
                            )

                        elif "play a game" in query:
                            from game import RockPaperScissorsGame
                            game = RockPaperScissorsGame()
                            game.play_game()


                        elif "screenshot" in query:
                            import pyautogui  # pip install pyautogui

                            im = pyautogui.screenshot()
                            im.save("ss.jpg")

                        elif "click my photo" in query:
                            pyautogui.press("super")
                            pyautogui.typewrite("camera")
                            # pyautogui.press("enter")
                            pyautogui.sleep(2)
                            self.speak("SMILE")
                            pyautogui.press("enter")

                        elif "focus mode" in query:
                            a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                            if (a == 1):
                                self.speak("Entering the focus mode....")
                                os.startfile("D:\\Projects\\Anni Ai Assisstant\\FocusMode.py")
                                exit()


                            else:
                                pass

                        elif "show my focus" in query:
                            from FocusGraph import focus_graph

                            focus_graph()

                        elif "translate" in query:
                            from Translator import TranslatorApp


                            translator_app = TranslatorApp()
                            query = query.replace("anni", "")
                            query = query.replace("translate", "")
                            translator_app.translategl(query)




                        elif "shutdown the system" in query:
                            self.speak("Are You sure you want to shutdown")
                            shutdown = input("Do you want to shutdown your computer? (yes/no)")
                            if shutdown == "yes":
                                os.system("shutdown /s /t 1")

                            elif shutdown == "no":
                                break

                        elif "time" in query:
                            strTime = datetime.datetime.now().strftime("%H:%M")
                            self.speak(f"Sir, the time is {strTime}")

                        elif "bye-bye" in query:
                            self.speak("Going to sleep,sir")
                            exit()
                            app = QApplication(sys.argv)
                            anni = Main()
                            anni.show()
                            sys.exit(app.exec_())

response_manager = ResponseManager()
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.movie = QtGui.QMovie("GIF/fxVE.gif")
        self.ui.circular_img.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("GIF/3aNC.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("GIF/3aNC.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("GIF/3aNC.gif")
        self.ui.tripent.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("GIF/J4o.gif")
        self.ui.rectline1.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("GIF/J4o.gif")
        self.ui.squaretri.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("GIF/J4o.gif")
        self.ui.squaretri_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("GIF/J4o.gif")
        self.ui.squaretri_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("GIF/J4o.gif")
        self.ui.squaretri_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("GIF/J4o.gif")
        self.ui.squaretri_5.setMovie(self.ui.movie)
        self.ui.movie.start()



        self.ui.movie = QtGui.QMovie("GIF/3aNC.gif")
        self.ui.tripen3.setMovie(self.ui.movie)
        self.ui.movie.start()

        startExecution.start()

app = QApplication(sys.argv)
anni = Main()
anni.show()
sys.exit(app.exec_())