from tkinter import messagebox, Label, Tk, ttk
from time import strftime
from pygame import mixer
import speech_recognition

class AlarmApp:
    def __init__(self):
        self.alarm_set = Tk()
        self.alarm_set.config(bg='black')
        self.alarm_set.geometry('500x250')
        self.alarm_set.title('Alarm')
        self.alarm_set.minsize(width=500, height=250)
        mixer.init()

        self.list_hours = [i for i in range(24)]
        self.list_minutes = [i for i in range(60)]
        self.list_seconds = [i for i in range(60)]

        self.create_gui()

    def create_gui(self):
        texto1 = Label(self.alarm_set, text='Hours', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
        texto1.grid(row=1, column=0, padx=5, pady=5)
        texto2 = Label(self.alarm_set, text='Minutes', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
        texto2.grid(row=1, column=1, padx=5, pady=5)
        texto3 = Label(self.alarm_set, text='Seconds', bg='black', fg='magenta', font=('Arial', 12, 'bold'))
        texto3.grid(row=1, column=2, padx=5, pady=5)

        self.box1 = ttk.Combobox(self.alarm_set, values=self.list_hours, style="TCombobox", justify='center',
                                 width='12', font='Arial')
        self.box1.grid(row=2, column=0, padx=15, pady=5)
        self.box1.current(0)
        self.box2 = ttk.Combobox(self.alarm_set, values=self.list_minutes, style="TCombobox", justify='center',
                                 width='12', font='Arial')
        self.box2.grid(row=2, column=1, padx=15, pady=5)
        self.box2.current(0)
        self.combobox3 = ttk.Combobox(self.alarm_set, values=self.list_seconds, style="TCombobox", justify='center',
                                      width='12', font='Arial')
        self.combobox3.grid(row=2, column=2, padx=15, pady=5)
        self.combobox3.current(0)

        style = ttk.Style()
        style.theme_create('combostyle', parent='alt', settings={'TCombobox': {'configure': {'selectbackground': 'red',
                                                                                            'fieldbackground': 'gold',
                                                                                            'background': 'blue'}}})
        style.theme_use('combostyle')

        self.alarm_set.option_add('*TCombobox*Listbox*Background', 'white')
        self.alarm_set.option_add('*TCombobox*Listbox*Foreground', 'black')
        self.alarm_set.option_add('*TCombobox*Listbox*selectBackground', 'green2')
        self.alarm_set.option_add('*TCombobox*Listbox*selectForeground', 'black')

        self.alarm_label = Label(self.alarm_set, fg='violet', bg='black', font=('Radioland', 20))
        self.alarm_label.grid(column=0, row=3, sticky="nsew", ipadx=5, ipady=20)

        self.repeat_label = Label(self.alarm_set, fg='white', bg='black', text='Repeated', font='Arial')
        self.repeat_label.grid(column=1, row=3, ipadx=5, ipady=20)

        self.cantidad = ttk.Combobox(self.alarm_set, values=(1, 2, 3, 4, 5), justify='center', width='8', font='Arial')
        self.cantidad.grid(row=3, column=2, padx=5, pady=5)
        self.cantidad.current(0)

        self.text_hour = Label(self.alarm_set, fg='green2', bg='black')
        self.text_hour.grid(columnspan=3, row=0, sticky="nsew", ipadx=5, ipady=20)

        self.set_time_part()
        self.alarm_set.mainloop()

    def set_time_part(self):
        x_hour = self.box1.get()
        x_minutes = self.box2.get()
        x_second = self.combobox3.get()
        hours = strftime('%H')
        minutes = strftime('%M')
        seconds = strftime('%S')

        total_hour = (hours + ' : ' + minutes + ' : ' + seconds)
        self.text_hour.config(text=total_hour, font=('Radioland', 25))
        hour_alarm = x_hour + ' : ' + x_minutes + ' : ' + x_second
        self.alarm_label['text'] = hour_alarm

        if int(hours) == int(x_hour) and int(minutes) == int(x_minutes) and int(seconds) == int(x_second):
            mixer.music.load("music.mp3")
            mixer.music.play(loops=int(self.cantidad.get()))
            close_command = self.take_command().lower()
            if "close alarm" in close_command:
                mixer.music.stop()
                self.alarm_set.destroy()

        self.text_hour.after(100, self.set_time_part)

    def take_command(self):
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
        return query

if __name__ == "__main__":
    app = AlarmApp()
