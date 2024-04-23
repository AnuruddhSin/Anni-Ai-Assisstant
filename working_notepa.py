import speech_recognition as sr
import subprocess

def open_notepad():
    subprocess.Popen(["notepad.exe"])

def close_notepad():
    subprocess.Popen(["taskkill", "/f", "/im", "notepad.exe"])

def write_note(note_text):
    with open("note.txt", "a") as file:
        file.write(note_text + "\n")

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()

                if "open notepad" in command:
                    open_notepad()

                elif "close notepad" in command:
                    close_notepad()

                elif "say that note" in command:
                    print("Listening for note content...")
                    note_audio = recognizer.listen(source, timeout=10)
                    note_text = recognizer.recognize_google(note_audio)
                    print(f"Note: {note_text}")
                    write_note(note_text)

                elif "save note" in command:
                    print("What name should I save the note as?")
                    note_name_audio = recognizer.listen(source, timeout=5)
                    note_name = recognizer.recognize_google(note_name_audio).lower()
                    with open(f"{note_name}.txt", "w") as file:
                        file.write(note_text)
                    print(f"Note saved as {note_name}.txt")

            except sr.UnknownValueError:
                print("Sorry, I didn't catch that. Can you please repeat?")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()
