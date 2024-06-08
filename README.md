# Anni Ai Assistant

Welcome to the Anni Ai Assistant repository! This project is a comprehensive AI assistant designed to help users with various tasks, including setting alarms, translating text, fetching news, and much more. The assistant comes with a graphical user interface and multiple Python scripts that handle different functionalities.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Anni Ai Assistant is an AI-powered virtual assistant that can perform a wide range of tasks. From setting alarms and reminders to fetching the latest news and telling jokes, Anni is designed to make your life easier. The project includes a GUI for easy interaction and several backend scripts that power the assistant's functionalities.

## Features

- **Alarm and Reminders**: Set and manage alarms.
- **News Reader**: Get the latest news updates.
- **Dictionary**: Look up word meanings.
- **Translation**: Translate text between different languages.
- **Focus Mode**: Tools to help you stay focused.
- **Games**: Simple games to play and relax.
- **Jokes**: Enjoy a variety of jokes.
- **Keyboard Automation**: Automate keyboard inputs.
- **Note Taking**: Create and manage notes.
- **WhatsApp Integration**: Automate WhatsApp messages.
- **OpenAI Integration**: Utilize OpenAI's capabilities for various tasks.

## Installation

To get started with Anni Ai Assistant, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/AnuruddhSin/Anni-Ai-Assisstant.git
    cd AnniAiAssistant
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the main script**:
    ```sh
    python main.py
    ```

## Usage

To use Anni Ai Assistant, follow these instructions:

1. **Run the main script**:
    ```sh
    python main.py
    ```

2. **Interact with the GUI**: Use the graphical user interface to access various functionalities of Anni Ai Assistant.

3. **Explore individual scripts**: Each script in the project directory handles a specific functionality. You can run these scripts independently if needed. For example:
    - To set an alarm, run:
      ```sh
      python alarm.py
      ```
    - To fetch news, run:
      ```sh
      python NewsRead.py
      ```

## Project Structure

Here is an overview of the project structure:

```
Anni Ai Assisstant/
│
├── .idea/                      # IDE configuration files
├── __pycache__/                # Compiled Python files
├── env/                        # Virtual environment
├── al.py                       # Alarm functionality
├── alarm.py                    # Alarm script
├── Alarmtext.txt               # Alarm text data
├── Calculatenumbers.py         # Calculator functionality
├── Dictapp.py                  # Dictionary application
├── FocusGraph.py               # Focus mode graph
├── FocusMode.py                # Focus mode functionality
├── game.py                     # Simple game script
├── GIF/                        # Directory for GIFs
├── GreetMe.py                  # Greeting script
├── gui_ai.py                   # AI GUI script
├── gui_anni.py                 # Main GUI script
├── gui_anni.ui                 # UI file for the GUI
├── hindi_jokes.py              # Hindi jokes script
├── INTRO.py                    # Introduction script
├── keyboard.py                 # Keyboard automation script
├── main.py                     # Main script to run the assistant
├── music.mp3                   # Background music
├── NewsRead.PY                 # News reading script
├── normal_talk.py              # Normal conversation script
├── open_ai_integration.py      # OpenAI integration script
├── password.txt                # Password file
├── Remember.txt                # Memory file
├── SearchNow.py                # Search functionality
├── ss.jpg                      # Screenshot
├── tasks.txt                   # Task list
├── temp_note.txt               # Temporary notes
├── Translator.py               # Translation functionality
├── Whatsapp.py                 # WhatsApp integration script
├── working_notepa.py           # Notepad functionality
├── z_score_outlier.py          # Outlier detection script
```

## Contributing

We welcome contributions from the community! If you would like to contribute to Anni Ai Assistant, please follow these steps:

1. **Fork the repository**: Click the "Fork" button at the top of this page to create a copy of this repository on your GitHub account.
2. **Clone the repository**: Clone your forked repository to your local machine.
    ```sh
    git clone https://github.com/AnuruddhSin/Anni-Ai-Assisstant.git
    ```
3. **Create a branch**: Create a new branch for your feature or bug fix.
    ```sh
    git checkout -b feature/YourFeatureName
    ```
4. **Make your changes**: Make the necessary changes to the code.
5. **Commit your changes**: Commit your changes with a clear and concise message.
    ```sh
    git commit -m "Anni_AI"
    ```
6. **Push to the branch**: Push your changes to your forked repository.
    ```sh
    git push origin feature/Anni_AI
    ```
7. **Create a pull request**: Open a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

We would like to thank the contributors and the open-source community for their support and contributions to this project.

---
